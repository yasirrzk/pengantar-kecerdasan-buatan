from flask import Flask, render_template, request, jsonify
import speech_recognition as srec
from gtts import gTTS
import pygame
import io
import subprocess
import webbrowser
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

MASTER = "Yasir"
driver = None  

def perintah():
    mendengar = srec.Recognizer()
    with srec.Microphone() as source:
        print('Mendengarkan.......')
        suara = mendengar.listen(source, phrase_time_limit=5)
        try:
            print('Diterima.......')
            dengar = mendengar.recognize_google(suara, language='id-ID')
            print(dengar)
        except Exception as e:
            print(f'Gagal mengenali suara: {e}')
            dengar = ""
        return dengar

def speak(teks):
    bahasa = 'id'
    suara = gTTS(text=teks, lang=bahasa, slow=False)

    mp3_fp = io.BytesIO()
    suara.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(mp3_fp, 'mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

def salam():
    sekarang = datetime.now()
    jam = sekarang.hour
    
    if 5 <= jam < 12:
        return f"Selamat Pagi, {MASTER}"
    elif 12 <= jam < 15:
        return f"Selamat Siang, {MASTER}"
    elif 15 <= jam < 18:
        return f"Selamat Sore, {MASTER}"
    else:
        return f"Selamat Malam, {MASTER}"

@app.route('/')
def index():
    sapaan = salam()
    print(f"Mengucapkan: {sapaan}")
    speak(sapaan)
    return render_template('index.html')

@app.route('/voice', methods=['POST'])
def voice():
    global driver
    Layanan = perintah()
    response = {"text": Layanan}
    if Layanan:
        if "buka chrome" in Layanan.lower():
            subprocess.Popen(['/usr/bin/google-chrome'])  
            speak("Buka Chrome")
            response["status"] = "Membuka Chrome"
        elif "buka spotify" in Layanan.lower():
            subprocess.Popen(['/snap/bin/spotify'])  
            speak("Buka Spotify")
            response["status"] = "Membuka Spotify" 
        elif "buka youtube" in Layanan.lower():
            webbrowser.open('https://www.youtube.com')
            speak("Buka Youtube")
            response["status"] = "Membuka Youtube"
        elif "login sinau" in Layanan.lower():
            if driver is None:
                driver = webdriver.Chrome()
            driver.get('https://syncnau.poltektegal.ac.id/login')

            username_field = driver.find_element(By.NAME, 'username')
            password_field = driver.find_element(By.NAME, 'password')
            login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

            username_field.send_keys('') 
            password_field.send_keys('') 

            login_button.click()

            speak("Login sinau")
            response["status"] = "Membuka Syncnau dan login"
    else:
        response["status"] = "Gagal mengenali suara"
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
