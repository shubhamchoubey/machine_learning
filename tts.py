from gtts import gTTS
import os

text=input("enter something : ")
tts = gTTS(text, lang='en')
tts.save('text.mp3')
os.system("mpg321 text.mp3")
