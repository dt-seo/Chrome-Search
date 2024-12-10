import pymysql
import glob
import os
from datetime import datetime

# En güncel dosyayı bulma
def get_latest_file(directory):
    files = glob.glob(os.path.join(directory, "*.txt"))
    if not files:
        print("Klasörde hiçbir .txt dosyası bulunamadı.")
        return None
    files.sort(key=os.path.getmtime, reverse=True)
    return files[0]  # En güncel dosya

# Dosya içeriklerini okuma
def load_file_content(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as file:
        return file.readlines()

# SQL veritabanına bağlanma ve verileri kaydetme
def save_to_database(data, script_start_time):
    try:
        # Veritabanı bağlantısı
        connection = pymysql.connect(
            host='212.31.2.93',
            user='remote',
            password="BIw883k8",
            database="search",
            charset='utf8mb4'
        )
        cursor = connection.cursor()

        # Verileri SQL'e kaydetme
        for row in data:
            sql = """
                INSERT INTO kesfetall (site_name, timestamp, news_time, headline)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    site_name=VALUES(site_name),
                    timestamp=VALUES(timestamp),
                    news_time=VALUES(news_time),
                    headline=VALUES(headline)
            """
            values = (row["Site"], script_start_time, row["Zaman"], row["Başlık"])
            cursor.execute(sql, values)

        connection.commit()
        print("Veriler başarıyla veritabanına kaydedildi.")
    except pymysql.MySQLError as e:
        print(f"Veritabanı hatası: {e}")
    finally:
        if connection and connection.open:
            cursor.close()
            connection.close()

# Ana işlem
if __name__ == "__main__":
    # Kodun başlama zamanı
    script_start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Dosya yolu
    directory_path = r"C:\Users\emir.usenmez\IdeaProjects\Search\Chrome-Search-main\Kesfet\corrected_text"
    latest_file = get_latest_file(directory_path)

    if not latest_file:
        print("En güncel dosya bulunamadı, işlem sonlandırılıyor.")
        exit()

    print(f"En güncel dosya: {latest_file}")
    content = load_file_content(latest_file)

    # Dosya içeriğini işleme
    data = []
    buffer = []
    for line in content:
        line = line.strip()  # Boşlukları kaldır
        if line:  # Boş satır değilse buffer'a ekle
            buffer.append(line)
        else:  # Boş satır gördüğümüzde, buffer'daki veriyi işlemeye çalış
            if len(buffer) == 3:  # Üç satırdan oluşuyorsa (Site, Zaman, Başlık)
                try:
                    site = buffer[0].split("Site:")[1].strip()
                    zaman = buffer[1].split("Zaman:")[1].strip()  # Zaman doğrudan alınır
                    baslik = buffer[2].split("Başlık:")[1].strip()
                    data.append({"Site": site, "Zaman": zaman, "Başlık": baslik})
                except Exception as e:
                    print(f"Satır işlenemedi: {buffer}, Hata: {e}")
            buffer = []  # Buffer'ı sıfırla

    # Eğer son satırlarda veri kaldıysa, onu da işle
    if len(buffer) == 3:
        try:
            site = buffer[0].split("Site:")[1].strip()
            zaman = buffer[1].split("Zaman:")[1].strip()  # Zaman doğrudan alınır
            baslik = buffer[2].split("Başlık:")[1].strip()
            data.append({"Site": site, "Zaman": zaman, "Başlık": baslik})
        except Exception as e:
            print(f"Satır işlenemedi: {buffer}, Hata: {e}")

    if not data:
        print("Dosyada işlenebilir veri bulunamadı, işlem sonlandırılıyor.")
        exit()

    print(f"İşlenebilir veri:\n{data}")

    # Veritabanına kaydetme
    save_to_database(data, script_start_time)
