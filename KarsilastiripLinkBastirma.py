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

openai.api_key = "api"

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
directory_path = "C:\\Users\\emir.usenmez\\IdeaProjects\\Search\\Chrome-Search-main\\Kesfet\\corrected_text"
last_two_files = get_last_two_corrected_files(directory_path)
if len(last_two_files) < 2:
    print("Yeterli sayıda dosya bulunamadı.")
    exit()

file_path_1, file_path_2 = last_two_files
content_first = load_file_content(file_path_1)
content_second = load_file_content(file_path_2)

def find_difference_between_lists(content_first, content_second):
    prompt = f"""
    Aşağıda iki farklı haber listesi bulunmaktadır. ikinci liste 'ikinci', ilk liste 'ilk' olarak adlandırılacaktır. 
    Lütfen 'ilk' listesinde yer alan ancak 'ikinci' listesinde yer almayan haberleri tespit edin ve listeleyin. Bu tespiti yaparken sadece Başlık kısmının bilgilerini dikkate alarak karşılaştırma yapınız. 
    Haber başlıkları tamamen aynı veya birbirine yakın olmalı, bu filtrede sadece 'ilk' dosyada olmayan haber başlıklarını listele. Haberlerin sıralamasının bir öenmi yok farklı sıralamada da aynı haber varsa eleyebilirsin.
    
    Eğer 'ikinci' listede yer alan bir haber, 'ilk' listede yer almıyorsa, o haberi şu formatta listeleyin:
    
    
    Site: [Site Adı]
    Zaman: [Zaman Bilgisi]
    Başlık: [Başlık İçeriği]
 
    ikinci Liste:
    {content_first}
    
    ilk Liste:
    {content_second}
    
    Yanıt formatı: 
    - Her haber için ayrı satırda, 'Site - Zaman - Başlık' şeklinde listeleyin.
    - Sadece 'ilk' listede olup 'ikinci' listede bulunmayan haberleri yazdırın.
    - Site_name kısmına başına '-' yazmayın.
    - hurriyet , milliyet ,vatan ,sözcü, ntv haber ,mynet ,posta ,sabah , big para gibi sitelerin yazımına dikkat et
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Haber içeriklerini karşılaştırın."},
                  {"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.2,
    )

    return response['choices'][0]['message']['content'].strip()

# Yeni haberleri bulma (İlk Liste'de olup İkinci Liste'de olmayanlar)
unique_news_text = find_difference_between_lists(content_first, content_second)
print("İlk Liste'deki haberler, İkinci Liste'de yer almayanlar:\n", unique_news_text)

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
def get_first_link(query, driver):
    # # işaretine kadar olan kısmı al
    if '#' in query:
        query = query.split('#')[0]  # #'den önceki kısmı al

    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    driver.get(search_url)

    time.sleep(2)

    link = None
    try:
        first_result = driver.find_element(By.CSS_SELECTOR, '[jscontroller="msmzHf"] a')
        link = first_result.get_attribute("href")
        # Linki # işaretine kadar almak için
        if link and '#' in link:
            link = link.split('#')[0]
    except Exception as e:
        print(f"Link bulunamadı: {e}")

    return link

# ChromeDriver'ı sadece bir kere başlatma
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Linkleri al ve DataFrame'e ekle
df["İlk Link"] = None
unique_links = set()  # Duplicates'ı engellemek için set kullanıyoruz
for index, row in df.iterrows():
    query = f" {row['Başlık']}"
    print(f"Aranıyor: {query}")
    link = get_first_link(query, driver)
    if link and link not in unique_links:
        unique_links.add(link)  # Aynı linki tekrar eklemiyoruz
        df.at[index, "İlk Link"] = link
    else:
        df.at[index, "İlk Link"] = "Link bulunamadı"
    time.sleep(2)

# Başlatılma zamanı ekleme (üç sütuna bölünmüş)
now = datetime.now()
df["timestamp"] = now.strftime("%Y-%m-%d %H:%M:%S")  # Tam tarih ve saat
df["date_only"] = now.strftime("%Y-%m-%d")            # Sadece tarih
df["time_only"] = now.strftime("%H:%M:%S")            # Sadece saat

# MySQL veritabanına bağlanma ve verileri kaydetme
def save_to_database(df):
    connection = None
    try:
        connection = pymysql.connect(
            host='212.31.2.93',
            user='remote',
            password="BIw883k8",
            database="search",  # Yeni veritabanı adı
            charset='utf8mb4'
        )
        cursor = connection.cursor()

        for _, row in df.iterrows():
            sql = ("\n"
                   "            INSERT INTO discoverdb (site_name, headline, timestamp, search_url, date_only, time_only) \n"
                   "            VALUES (%s, %s, %s, %s, %s, %s)\n"
                   "            ON DUPLICATE KEY UPDATE \n"
                   "                site_name=VALUES(site_name), \n"
                   "                headline=VALUES(headline),\n"
                   "                timestamp=VALUES(timestamp),\n"
                   "                search_url=VALUES(search_url),\n"
                   "                date_only=VALUES(date_only),\n"
                   "                time_only=VALUES(time_only)\n"
                   "            ")
            values = (row['Site'], row['Başlık'], row['timestamp'], row['İlk Link'], row['date_only'], row['time_only'])
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

# WebDriver'ı kapatma
driver.quit()
