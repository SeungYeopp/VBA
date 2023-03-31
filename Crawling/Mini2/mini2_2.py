from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
from bs4 import BeautifulSoup


query = input("검색어를 입력하세요: ")


url = 'https://www.google.com/'
# 크롬 드라이버의 위치 설정
driver = webdriver.Chrome('C:/chromedirver/chromedriver.exe')
driver.get(url)
time.sleep(1)


# 구글 검색 창에 입력한 검색어를 검색
search_box = driver.find_element(By.CSS_SELECTOR, 'input[name="q"]')
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(1)


# 동영상 탭으로 이동
driver.find_element(By.XPATH, '//a[text()="동영상"]').click()
time.sleep(1)


# 이동한 페이지의 url을 저장 후 BS를 이용하여 html을 잘 정리된 형태로 변환
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


cnt = 1
# div 태그 아래 class이름이 VYkpsb고, data-stfc="1"인 값들을 찾고, 반복문을 돌며 비디오를 해당 위치에 저장
for video in soup.select('div.VYkpsb[data-stfc="1"]'):
   # print(video)
   urllib.request.urlretrieve(video['data-url'], query + str(cnt) + '.mp4')
   cnt += 1


# 브라우저 종료
driver.quit()
