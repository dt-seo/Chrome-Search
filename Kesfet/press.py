import subprocess
import pytesseract
from PIL import Image, ImageFilter
import time
import openai
import os
from datetime import datetime

openai.api_key = "api"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

log_file = "C:\\Users\\testname\\Contacts\\KESFET\\a.txt"

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

def scroll_down(scroll_distance=1150):
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
    restart_browser()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    initial_screenshot_filename = f"screenshot_initial_{timestamp}.png"
    take_screenshot(initial_screenshot_filename)

    all_text = []
    processed_image = preprocess_image(initial_screenshot_filename)
    text = pytesseract.image_to_string(processed_image, lang="tur")
    all_text.append(text)

    for i in range(1, 10):
        scroll_down(scroll_distance=1150)
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

    output_filename = f"corrected_text_{timestamp}.txt"
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(corrected_text)

    print(f"Düzeltilmiş metin '{output_filename}' dosyasına kaydedildi.")

# capture_and_process() fonksiyonunu çalıştır
capture_and_process()
