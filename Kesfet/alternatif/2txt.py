import openai

openai.api_key = "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"

def load_file_content(file_path):
    """Dosyanın içeriğini okur ve döndürür."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

file_path_1 = "C:\\Users\\testname\\Contacts\\Kesfet\\corrected_text_20241111_100312.txt"
file_path_2 = "C:\\Users\\testname\\Contacts\\Kesfet\\corrected_text_20241111_101617.txt"

# Dosyaların içeriğini yükle
content_first = load_file_content(file_path_1)
content_second = load_file_content(file_path_2)

# API üzerinden karşılaştırma yapmak için istekte bulun
def find_unique_news(content_first, content_second):
    prompt = f"""
    Aşağıda iki farklı haber listesi bulunmaktadır. İlk liste, 'İlk Liste' ve ikinci liste 'İkinci Liste' olarak adlandırılmıştır. Lütfen 'İkinci Liste'de yer alıp 'İlk Liste'de olmayan haberleri tespit edin.
    
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
        max_tokens=2000,
        temperature=0.2,
    )
    
    return response['choices'][0]['message']['content'].strip()

# Karşılaştırma sonucunu al ve yazdır
unique_news = find_unique_news(content_first, content_second)
print("İlk dosyada bulunmayan ve yalnızca ikinci dosyada olan haberler:\n")
print(unique_news)
