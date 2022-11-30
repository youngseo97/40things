from gtts import gTTS
from playsound import playsound as ps
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "안녕하세용 "

tts = gTTS(text=text, lang='ko')
tts.save("hi.mp3")

ps("hi.mp3")
