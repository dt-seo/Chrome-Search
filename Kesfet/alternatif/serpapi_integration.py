import openai
import pandas as pd
from datetime import datetime
from serpapi import GoogleSearch
import time

openai.api_key = "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"
SERPAPI_API_KEY = "2b792260e0fbb4a7413fb156829616b4f6fe831928bdd871ed49e29dd50e71bd"

def extract_news_sites_and_titles(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Metindeki tüm haber sitelerini, her sitenin yanında yer alan haber başlıkları ve zaman bilgisi ile birlikte orijinal sıralamada listele. Lütfen sıralamayı bozmadan ve siteleri kümelendirmeden, metinde bulundukları sırayla listele. Çıktı formatı 'Site - Zaman - Başlık' şeklinde olsun."},
            {"role": "user", "content": text},
        ],
        max_tokens=2000,
        temperature=0.2
    )
    return response['choices'][0]['message']['content'].strip()

def get_first_link(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    
    # Arama sonuçlarından ilk URL'yi çekme
    if "organic_results" in results and len(results["organic_results"]) > 0:
        return results["organic_results"][0]["link"]
    return None

# Dosya yolunu tanımlayın
input_file_path = "C:\\Users\\testname\\Contacts\\Kesfet\\corrected_text_20241107_102043.txt"

# Dosyayı oku
with open(input_file_path, "r", encoding="utf-8") as file:
    input_text = file.read()

# Metindeki haber sitelerini, zamanları ve başlıkları tespit et
news_sites_and_titles = extract_news_sites_and_titles(input_text)

# OpenAI API'den dönen cevabı doğrudan yazdırarak kontrol edin
print("OpenAI'den dönen yanıt:\n", news_sites_and_titles)

# Çıktıyı satır satır işle ve Site, Zaman, Başlık bilgilerini doğru sırada ayır
data = []
for line in news_sites_and_titles.split('\n'):
    if " - " in line:
        parts = line.split(" - ")
        if len(parts) == 3:
            site, time_info, title = parts  # Site, Zaman, Başlık sırasını koruyoruz
            data.append({"Site": site.strip(), "Zaman": time_info.strip(), "Başlık": title.strip()})

# Eğer data boşsa, API'nin yanıtında bir sorun olabilir.
if not data:
    print("API'den alınan veri işlenemedi. Yanıt formatını kontrol edin.")
else:
    # DataFrame oluştur
    df = pd.DataFrame(data)
    
    # Her bir satır için A ve C sütunlarını birleştirip arama yap ve ilk linki al
    df["İlk Link"] = None  # Yeni bir sütun oluştur
    for index, row in df.iterrows():
        query = f"{row['Site']} {row['Başlık']}"
        print(f"Aranıyor: {query}")
        
        # İlk çıkan linki al ve 'İlk Link' sütununa yaz
        link = get_first_link(query)
        df.at[index, "İlk Link"] = link
        
        # Google bot koruma sisteminden kaçınmak için bekleyin
        time.sleep(2)
    
    # Bugünün tarihine göre dosya adını oluştur (tarih ve saat eklenmiş halde)
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file_path = f"C:\\Users\\testname\\Contacts\\Kesfet\\haber_siteleri_ve_basliklar_{now}.xlsx"
    
    # Verileri Excel dosyasına sırayla kaydet
    df.to_excel(output_file_path, index=False)
    print(f"Haber siteleri, başlıklar ve ilk çıkan linkler '{output_file_path}' dosyasına kaydedildi.")
