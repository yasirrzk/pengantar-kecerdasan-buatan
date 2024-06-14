# from flask import Flask, render_template, request, jsonify
# import speech_recognition as srec
# from gtts import gTTS
# import pygame
# import io

# app = Flask(__name__)

# def perintah():
#     mendengar = srec.Recognizer()
#     with srec.Microphone() as source:
#         print('Mendengarkan.......')
#         suara = mendengar.listen(source, phrase_time_limit=5)
#         try:
#             print('Diterima.......')
#             dengar = mendengar.recognize_google(suara, language='id-ID')
#             print(dengar)
#         except:
#             print('Gagal mengenali suara.')
#             dengar = ""
#         return dengar

# def ngomong(teks):
#     bahasa = 'id'
#     suara = gTTS(text=teks, lang=bahasa, slow=False)

#     # Menyimpan suara ke dalam buffer
#     mp3_fp = io.BytesIO()
#     suara.write_to_fp(mp3_fp)
#     mp3_fp.seek(0)

#     # Menggunakan pygame untuk memutar audio
#     pygame.mixer.init()
#     pygame.mixer.music.load(mp3_fp, 'mp3')
#     pygame.mixer.music.play()

#     while pygame.mixer.music.get_busy():
#         continue

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/voice', methods=['POST'])
# def voice():
#     Layanan = perintah()
#     if Layanan:
#         ngomong(Layanan)
#     return jsonify({"text": Layanan})

# if __name__ == '__main__':
#     app.run(debug=True)
    

# import speech_recognition as srec
# from gtts import gTTS
# import os

# def perintah():
#     mendengar = srec.Recognizer()
#     with srec.Microphone() as source:
#         print('Mendengarkan.......')
#         suara = mendengar.listen(source, phrase_time_limit=5)
#         try:
#             print('Diterima.......')
#             dengar = mendengar.recognize_google(suara, language='id-ID')
#             print(dengar)
#         except:
#             print('Gagal mengenali suara.')
#             dengar = ""
#         return dengar
        
# def ngomong(self):
#     teks =self
#     bahasa = 'id'
#     namaFile = 'ngomong.mp3'
#     def reading():
#         suara =gTTS(text=teks, lang=bahasa, slow=False)
#         suara.save(namaFile)
#         os.system(f'xdg-open {namaFile}')
#     reading()        

# def run_yaseru():
#     Layanan = perintah()
#     print(Layanan)  

# run_yaseru()

# import speech_recognition as srec
# from gtts import gTTS
# import pygame
# import io

# def perintah():
#     mendengar = srec.Recognizer()
#     with srec.Microphone() as source:
#         print('Mendengarkan.......')
#         suara = mendengar.listen(source, phrase_time_limit=5)
#         try:
#             print('Diterima.......')
#             dengar = mendengar.recognize_google(suara, language='id-ID')
#             print(dengar)
#         except:
#             print('Gagal mengenali suara.')
#             dengar = ""
#         return dengar

# def ngomong(teks):
#     bahasa = 'id'
#     suara = gTTS(text=teks, lang=bahasa, slow=False)
    
#     # Menyimpan suara ke dalam buffer
#     mp3_fp = io.BytesIO()
#     suara.write_to_fp(mp3_fp)
#     mp3_fp.seek(0)
    
#     # Menggunakan pygame untuk memutar audio
#     pygame.mixer.init()
#     pygame.mixer.music.load(mp3_fp, 'mp3')
#     pygame.mixer.music.play()

#     while pygame.mixer.music.get_busy():
#         continue

# def run_yaseru():
#     Layanan = perintah()
#     if Layanan:
#         ngomong(Layanan)
#     print(Layanan)  

# if __name__ == "__main__":
#     run_yaseru()
