from flask import Flask, render_template, request, jsonify
import speech_recognition as srec
from gtts import gTTS
import pygame
import io

app = Flask(__name__)

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

def ngomong(teks):
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/voice', methods=['POST'])
def voice():
    Layanan = perintah()
    response = {"text": Layanan}
    if Layanan:
        ngomong(Layanan)
        response["status"] = "Diterima"
    else:
        response["status"] = "Gagal mengenali suara"
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)