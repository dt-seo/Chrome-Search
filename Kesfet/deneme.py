import openai
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pymysql
import glob
import os

openai.api_key = 'api'
# Dosya içeriklerini yükleyen fonksiyon
def load_file_content(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Son iki "corrected_text" dosyasını bulma
def get_last_two_corrected_files(directory):
    files = glob.glob(os.path.join(directory, "corrected_text_*.txt"))
    files.sort(key=os.path.getmtime, reverse=True)
    return files[:2] if len(files) >= 2 else []

# Dosya yollarını otomatik olarak belirleme
directory_path = "C:\\Users\\testname\\Contacts\\Kesfet"
last_two_files = get_last_two_corrected_files(directory_path)
if len(last_two_files) < 2:
    print("Yeterli sayıda dosya bulunamadı.")
    exit()

file_path_1, file_path_2 = last_two_files
content_first = load_file_content(file_path_1)
content_second = load_file_content(file_path_2)

def find_unique_news(content_first, content_second):
    prompt = f"""
    Aşağıda iki farklı haber listesi bulunmaktadır. İlk liste, 'İlk Liste' ve ikinci liste 'İkinci Liste' olarak adlandırılmıştır. 
    Lütfen 'İkinci Liste'de yer alıp 'İlk Liste'de olmayan haberleri tespit edin ve listeleyin.
    
    İlk Liste:
    {content_first}
    
    İkinci Liste:
    {content_second}
    
    Yanıt formatı: 'Site - Zaman - Başlık' şeklinde her bir yeni haber için ayrı satır.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Haber içeriklerini karşılaştırın."},
                  {"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.2,
    )
    
    return response['choices'][0]['message']['content'].strip()

# Yeni haberleri bulma
unique_news_text = find_unique_news(content_first, content_second)
print("Yeni haberler:\n", unique_news_text)

# Eğer unique_news_text boşsa işlem durduruluyor
if not unique_news_text.strip():
    print("Yeni haber bulunamadı, veritabanına kaydedilecek bir şey yok.")
    exit()

# DataFrame oluşturma
data = []
for line in unique_news_text.split('\n'):
    if " - " in line:
        parts = line.split(" - ")
        if len(parts) == 3:
            site, zaman, baslik = parts
            data.append({"Site": site.strip(), "Zaman": zaman.strip(), "Başlık": baslik.strip()})

df = pd.DataFrame(data)

# Google'da ilk linki bulma fonksiyonu
def get_first_link(query):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    driver.get(search_url)
    
    time.sleep(2)
    
    link = None
    try:
        first_result = driver.find_element(By.CSS_SELECTOR, '[jscontroller="msmzHf"] a')
        link = first_result.get_attribute("href")
    except Exception as e:
        print(f"Link bulunamadı: {e}")
    
    driver.quit()
    return link

# Linkleri al ve DataFrame'e ekle
df["İlk Link"] = None
for index, row in df.iterrows():
    query = f"{row['Site']} {row['Başlık']}"
    print(f"Aranıyor: {query}")
    link = get_first_link(query)
    df.at[index, "İlk Link"] = link if link else "Link bulunamadı"
    time.sleep(2)

# Başlatılma zamanı ekleme (üç sütuna bölünmüş)
now = datetime.now()
df["datetime_recorded"] = now.strftime("%Y-%m-%d %H:%M:%S")  # Tam tarih ve saat
df["date_only"] = now.strftime("%Y-%m-%d")                   # Sadece tarih
df["time_only"] = now.strftime("%H:%M:%S")                   # Sadece saat

# MySQL veritabanına bağlanma ve verileri kaydetme
def save_to_database(df):
    connection = None  # Bu satır eklendi
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password="moY4f1",
            database="search_db",
            charset='utf8mb4'
        )
        cursor = connection.cursor()

        for _, row in df.iterrows():
            sql = """
            INSERT INTO search (site_name, headline, datetime_recorded, search_url, date_only, time_only) 
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                site_name=VALUES(site_name), 
                headline=VALUES(headline),
                datetime_recorded=VALUES(datetime_recorded),
                search_url=VALUES(search_url),
                date_only=VALUES(date_only),
                time_only=VALUES(time_only)
            """
            values = (row['Site'], row['Başlık'], row['datetime_recorded'], row['İlk Link'], row['date_only'], row['time_only'])
            cursor.execute(sql, values)

        connection.commit()
        print("Veriler başarıyla veritabanına kaydedildi.")
    except pymysql.MySQLError as err:
        print(f"Veritabanı hatası: {err}")
    finally:
        if connection and connection.open:
            cursor.close()
            connection.close()

# Veritabanına kaydetme işlemini çağırma
save_to_database(df)
