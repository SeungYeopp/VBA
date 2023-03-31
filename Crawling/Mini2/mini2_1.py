from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
from bs4 import BeautifulSoup

query = input("검색어를 입력하세요: ")

url = 'https://www.naver.com/'
# 크롬 드라이버의 위치 설정
driver = webdriver.Chrome('C:/chromedirver/chromedriver.exe')
driver.get(url)
time.sleep(1)

# 네이버 검색 창에 입력한 검색어를 검색
search_box = driver.find_element(By.CSS_SELECTOR, "input#query")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(1)

# 이미지 탭으로 이동
driver.find_element(By.XPATH, '//a[text()="이미지"]').click()
time.sleep(1)

# 이동한 페이지의 url을 저장 후 BS를 이용하여 html을 잘 정리된 형태로 변환
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

cnt = 1
# img태그를 가지고 있는 것을 총 10개 찾고, 반복문을 돌며 이미지 파일 해당 위치에 저장
for image in soup.select('img._image._listImage', limit=10):
    urllib.request.urlretrieve(image['src'], query + str(cnt) + '.jpg')
    cnt += 1

# 브라우저 종료
driver.quit()