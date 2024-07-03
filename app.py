from flask import Flask, render_template, request, jsonify
import speech_recognition as srec
from gtts import gTTS
import pygame
import io
import subprocess
import webbrowser
from datetime import datetime

app = Flask(__name__)

MASTER = "Yasir"

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

    # Menyimpan suara ke dalam buffer
    mp3_fp = io.BytesIO()
    suara.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    # pygame untuk memutar audio
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
    elif 12 <= jam < 18:
        return f"Selamat Siang, {MASTER}"
    elif 18 <= jam < 21:
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
    Layanan = perintah()
    response = {"text": Layanan}
    if Layanan:
        if "buka chrome" in Layanan.lower():
            subprocess.Popen(['/usr/bin/google-chrome'])  
            speak("buka Chrome")
            response["status"] = "Membuka Chrome"
        elif "buka spotify" in Layanan.lower():
            subprocess.Popen(['/snap/bin/spotify'])  
            speak("Buka Spotify")
            response["status"] = "Membuka Spotify" 
        elif "buka youtube" in Layanan.lower():
            webbrowser.open('https://www.youtube.com')
            speak("Buka Youtube")
            response["status"] = "Membuka Youtube"
        else:
            speak(Layanan)
            response["status"] = "Diterima"
    else:
        response["status"] = "Gagal mengenali suara"
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
