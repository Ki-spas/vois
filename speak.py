import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from  deep_translator import GoogleTranslator 
import pyttsx3 

duration = 5  # секунды записи
sample_rate = 44100

print("Говори...")
recording = sd.rec(
  int(duration * sample_rate), # длительность записи в сэмплах
  samplerate=sample_rate,      # частота дискретизации
  channels=1,                  # 1 — это моно
  dtype="int16")               # формат аудиоданных
sd.wait()  # ждём завершения записи
wav.write("output.wav", sample_rate, recording)
print("Запись завершена, теперь распознаём...")

recognizer = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)
try:
    text = recognizer.recognize_google(audio, language="ru-RU")
    print("Ты сказал:", text , )
except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
    print("Не удалось распознать речь.")
except sr.RequestError as e:             # - если нет интернета или API недоступен
    print(f"Ошибка сервиса: {e}")

def translates(text):
    translate =  GoogleTranslator(source='auto' , target= 'en').translate(text)
    return translate 




p = translates(text)
print( "Перевод " + p)
print("oзвучиваем...")
engine = pyttsx3.init()
engine.setProperty('rate', 90)
engine.say( p )
engine.runAndWait()