import requests
from bs4 import BeautifulSoup
from selenium import webdriver

print("KRW=한국(원), USD=미국(달러), JPY=일본(엔), EUR=유럽(유로)")
#드라이버설정
# driver = webdriver.Chrome(executable_path="C:\dev\python\webdriver\chromedriver.exe")

def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1,target2), headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/main/div/div[1]/div[2]/div[1]/span').text.strip()
    print(containers)

get_exchange_rate('usd','krw')
# get_exchange_rate(input("여기에 첫국가를 입력해주세요"),input("두번째 국가입력 해주세요"))

#오류
#[1]urllib.error.HTTPError: HTTP Error 403: Forbidden을 headers={'User-Agent': 'Mozilla/5.0'}을 url뒤에 넣어줘서 해결