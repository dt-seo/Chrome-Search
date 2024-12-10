import subprocess
import pytesseract
from PIL import Image, ImageFilter
import time
import openai
import os
from datetime import datetime
import glob

openai.api_key = "spi"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

log_file = "C:\\Users\\emir.usenmez\\IdeaProjects\\Search\\a.txt"

def is_emulator_running():
    """Emülatörün açık olup olmadığını kontrol eder."""
    try:
        result = subprocess.run(["adb", "devices"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Çıktı 'List of devices attached' ile başlar ve çalışan cihazlar listelenir
        if "emulator" in result.stdout:
            print("Emülatör açık.")
            return True
        else:
            print("Emülatör açık değil.")
            return False
    except Exception as e:
        print(f"Emülatör durumu kontrol edilemedi: {e}")
        return False

def start_emulator():
    """Emülatör başlatır."""
    emulator_command = r"C:\Users\emir.usenmez\AppData\Local\Android\Sdk\emulator\emulator -avd Medium_Phone_API_35 -netdelay none -netspeed full"
    print("Emülatör başlatılıyor...")
    subprocess.Popen(emulator_command, shell=True)
    time.sleep(180)  # Emülatörün tam olarak başlatılması için 3 dakika bekleme

def ensure_emulator_running():
    """Eğer emülatör açık değilse başlatır."""
    if not is_emulator_running():
        start_emulator()
    else:
        print("Emülatör zaten açık, yeniden başlatmaya gerek yok.")

def restart_browser():
    print("Tarayıcı yeniden başlatılıyor...")
    subprocess.run(["adb", "shell", "am", "force-stop", "com.android.chrome"])
    time.sleep(1)
    subprocess.run(["adb", "shell", "am", "start", "-n", "com.android.chrome/com.google.android.apps.chrome.Main"])
    time.sleep(15)  # Program başlatıldıktan sonra 15 saniye bekleme

def refresh_page():
    print("Sayfa yenileniyor...")
    subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_F5"])

def take_screenshot(filename):
    print(f"Ekran görüntüsü alınıyor ve {filename} dosyasına kaydediliyor...")
    subprocess.run(["adb", "shell", "screencap", "-p", f"/sdcard/{filename}"])
    subprocess.run(["adb", "pull", f"/sdcard/{filename}", filename])

def scroll_down(scroll_distance=1900):
    print(f"Sayfa {scroll_distance} piksel kaydırılıyor...")
    subprocess.run(["adb", "shell", "input", "swipe", "500", str(1500), "500", str(1500 - scroll_distance)])
    time.sleep(3)

def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.convert('L')
    image = image.filter(ImageFilter.MedianFilter())
    image = image.filter(ImageFilter.SHARPEN)
    threshold = 128
    image = image.point(lambda p: p > threshold and 255)
    return image

def correct_text_with_openai(text):
    prompt = f"""
    Aşağıda yer alan metindeki haberleri düzenleyin ve her bir haber için aşağıdaki formatı kullanarak sıralayın:
    Zaman bilgi site adının yanında ne yazıyorsa aynı şekilde yazılsı bu veri sadece sayı ve günse g saatse s vb olacak şekilde düzenlensin.
    
    1. Site: [Site Adı]
       Zaman: [Zaman Bilgisi - Sitede görünen şekliyle]
       Başlık: [Başlık İçeriği]
       
    Metin:
    {text}
    
    Bu formatı takip edin ve her haberi sırasıyla numaralandırarak listeleyin. 
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000,
        temperature=0.2
    )
    return response['choices'][0]['message']['content'].strip()

def capture_and_process():
    ensure_emulator_running()  # Emülatörün açık olup olmadığını kontrol et ve gerekirse başlat
    restart_browser()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    initial_screenshot_filename = f"xscreenshot_initial_{timestamp}.png"
    take_screenshot(initial_screenshot_filename)

    all_text = []
    processed_image = preprocess_image(initial_screenshot_filename)
    text = pytesseract.image_to_string(processed_image, lang="tur")
    all_text.append(text)

    for i in range(1, 10):
        scroll_down(scroll_distance=1800)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_filename = f"screenshot_{i}_{timestamp}.png"
        take_screenshot(screenshot_filename)

        processed_image = preprocess_image(screenshot_filename)
        text = pytesseract.image_to_string(processed_image, lang="tur")
        all_text.append(text)

        os.remove(screenshot_filename)

    full_text = "\n".join(all_text)
    print("Çıkarılan Tüm Metin:\n", full_text)

    corrected_text = correct_text_with_openai(full_text)
    print("\nDüzeltilmiş Metin:\n", corrected_text)

    # Kaydedilecek dosyanın tam yolunu belirleyin
    output_filename = f"C:\\Users\\emir.usenmez\\IdeaProjects\\Search\\Chrome-Search-main\\Kesfet\\corrected_text\\corrected_text_{timestamp}.txt"
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(corrected_text)

    print(f"Düzeltilmiş metin '{output_filename}' dosyasına kaydedildi.")


def stop_emulator():
    """Emülatörü kapatır."""
    try:
        result = subprocess.run(["adb", "devices"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        devices_output = result.stdout.splitlines()

        # Emülatör cihazlarını bul
        emulator_ids = [line.split()[0] for line in devices_output if "emulator" in line]

        if emulator_ids:
            for emulator_id in emulator_ids:
                print(f"Emülatör {emulator_id} kapatılıyor...")
                subprocess.run(["adb", "-s", emulator_id, "emu", "kill"], check=True)
            print("Emülatör başarıyla kapatıldı.")
        else:
            print("Emülatör açık değil.")
    except Exception as e:
        print(f"Emülatör kapatılırken hata oluştu: {e}")

        # Dosyaları silme fonksiyonu
def delete_xscreenshot_files(directory):
    # xscreenshot_initial ile başlayan tüm dosyaları bulma
    files_to_delete = glob.glob(os.path.join(directory, "xscreenshot_initial*"))

    # Dosyaları silme
    for file in files_to_delete:
        try:
            os.remove(file)
            print(f"Silindi: {file}")
        except Exception as e:
            print(f"Dosya silinirken hata oluştu: {e}")

# Klasör yolunu belirleyin
directory_path = "C:\\Users\\emir.usenmez\\IdeaProjects\\Search\\Chrome-Search-main\\Kesfet"


if __name__ == "__main__":
    capture_and_process()  # Ekran görüntüsü al ve işle
    stop_emulator()  # Emülatörü kapat
delete_xscreenshot_files(directory_path) # xscreenshot_initial ile başlayan dosyaları sil
