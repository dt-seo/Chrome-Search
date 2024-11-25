import pandas as pd
import pymysql

# CSV dosyasını yükleme
csv_file = "saa.csv"  # CSV dosyanızın yolu
data = pd.read_csv(csv_file)

# MySQL bağlantısı
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='moY4f1',  # Şifrenizi yazın
    database='search',
    charset='utf8mb4'
)

# Verileri SQL'e ekleme
try:
    with connection.cursor() as cursor:
        for _, row in data.iterrows():
            sql = """
            INSERT INTO search (site_name, headline, timestamp, search_url, date_only, time_only)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                row['site_name'],
                row['headline'],
                row['timestamp'],
                row['search_url'],
                row['date_only'],
                row['time_only']
            ))
        connection.commit()
        print("Veriler başarıyla eklendi.")
except Exception as e:
    print(f"Hata oluştu: {e}")
finally:
    connection.close()
