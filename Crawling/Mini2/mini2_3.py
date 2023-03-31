from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytube import YouTube

query = input("검색어를 입력하세요: ")

url = 'https://www.google.com/'
# 크롬 드라이버의 위치 설정
driver = webdriver.Chrome('C:/chromedirver/chromedriver.exe')
driver.get(url)
time.sleep(1)

# 'q'라는 이름을 가진 입력 요소가 로드 될 때까지 최대 10 초간 기다림
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'q'))
)
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(1)

# 동영상 탭으로 이동
driver.find_element(By.XPATH, '//a[text()="동영상"]').click()
time.sleep(1)

# 이동한 페이지의 url을 저장 후 BS를 이용하여 html을 잘 정리된 형태로 변환
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 동영상 링크로 들어가기 위해 GyAeWb 클래스 내에 있는 https:// 링크 찾기
for link in soup.select('div.GyAeWb a[href^="https://"]', limit = 20):
    href = link['href']
    driver.get(href)
    ch_url = driver.page_source
    soup1 = BeautifulSoup(ch_url, 'html.parser')
    embed_link = ""

    # 링크가 youtube로 시작할 때
    if "https://www.youtube.com" in driver.current_url:
        watch_link = driver.current_url
        youtube_link = YouTube(watch_link)
        youtube_link.streams.get_highest_resolution().download()
    # 링크가 youtube가 아닌 일반 사이트일 때
    else:
        # iframe 들어있는 youtube.com/embed/ 링크를 실제 링크로 변환 후 동영상 다운로드
        for video in soup1.select('iframe[src^="https://www.youtube.com/embed/"]'):
            embed_link = video['src']
            watch_link = embed_link.replace('/embed/', '/watch?v=')

            # 동영상 다운로드
            youtube_link = YouTube(watch_link)
            youtube_link.streams.get_highest_resolution().download()

# 브라우저 종료
driver.quit()