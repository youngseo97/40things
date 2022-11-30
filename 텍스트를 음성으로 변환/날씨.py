from selenium import webdriver
from bs4 import BeautifulSoup
import time


#웹브라우저 설정
driver = webdriver.Chrome(executable_path="C:\dev\python\webdriver\chromedriver.exe")
#지역입력
area = input("지역을 입력해주세욧 :")

#사이트 주소 url
url='https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={}+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hGeOEsp0J1sssCqcjdNssssssTG-208199'.format(area)
driver.get(url)
driver.maximize_window()
#2초대기
time.sleep(2)

# #html코드 따오기
# result = []
# result = [['연도', '순위', '제목', '가수', '장르']]
#
#
#     #노래제목
#     for i in range(1,3) :
#         driver.get(url)
#
#         try:
#             #메인페이지 html
#             html = driver.page_source
#             soup = BeautifulSoup(html, "html.parser")
#
#             # 순위미다 tbody/tr[i]이다름
#             #노래제목
#             music_name = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/div[4]/div/div[2]/div[1]/form/table/tbody/tr[%d]/td[4]/div/div/div[1]/span/strong/a"%i).text.strip()
#             time.sleep(0.5)
#
#             #상세보기 페이지 이동
#
#             more_info_list = driver.find_element_by_xpath('/html/body/div/div[3]/div/div/div[4]/div/div[2]/div[1]/form/table/tbody/tr[%d]/td[4]/div/a'%i).click()
#
#             #상세페이지 html코드 따오기
#             html = driver.page_source
#             soup = BeautifulSoup(html,"html.parser")
#
#             #상세페이지에서 가수와 장르
#             singer = soup.select("div.artist>a>span")[0].text.strip()
#             ganre = soup.select("div.meta > dl > dd:nth-child(6)")[0].text.strip()
#
#             rank=i
#             #리설트 클래스에 값저장
#             result.append([year[y],rank,music_name,singer,ganre])
#             time.sleep(0.5)
#
#         except :
#             continue
#     csvuse.writecsv('year({})_songs.csv'.format(year[y]),result)
#
# print(result)


