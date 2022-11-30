from gtts import gTTS
from playsound import playsound as ps
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path ='test.txt'
with open(file_path, 'rt', encoding= 'UTF8') as f :
    read_file = f.read()

tts = gTTS(text=read_file , lang='ko')
tts.save("test.mp3")

ps("test.mp3")
