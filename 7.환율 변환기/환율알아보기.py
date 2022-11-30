import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from gtts import gTTS
from playsound import playsound as ps
from datetime import datetime
import os


print("KRW=한국(원), USD=미국(달러), JPY=일본(엔), EUR=유럽(유로)")

options = webdriver.ChromeOptions()
options.add_argument('headless')

#드라이버설정
driver = webdriver.Chrome(executable_path="C:\dev\python\webdriver\chromedriver.exe", chrome_options=options)

target1 = input("여기에 첫국가를 입력해주세요 : ")
target2 = 'krw'

if target1 == 'usd' :
    c='미국'
elif target1 == 'jpy' :
    c='일본'
elif target1 == 'eur' :
    c='유럽'


url="https://kr.investing.com/currencies/{}-{}".format(target1,target2)
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
exchange = soup.select("#__next > div > div > div > div.grid.gap-4.tablet\:gap-6.grid-cols-4.tablet\:grid-cols-8.desktop\:grid-cols-12.grid-container--fixed-desktop.general-layout_main__lRLYJ > main > div > div.instrument-header_instrument-header__y2HCk.mb-5.bg-background-surface.tablet\:grid.tablet\:grid-cols-2 > div:nth-child(2) > div.instrument-price_instrument-price__xfgbB.flex.items-end.flex-wrap.font-bold > span")[0].text.strip()
print("현재 1000원(KRW)기준으로 {}입니다".format(exchange))
ex=exchange
now=datetime.now()
h=now.hour
m=now.minute
text="현재 {}시{}분 {}와의 환율은 {}원 입니다".format(h,m,c,ex)

tts = gTTS(text=text, lang='ko')
tts.save("exchange.mp3")

ps("exchange.mp3")

#오류
#[1]urllib.error.HTTPError: HTTP Error 403: Forbidden을 headers={'User-Agent': 'Mozilla/5.0'}을 url뒤에 넣어줘서 해결