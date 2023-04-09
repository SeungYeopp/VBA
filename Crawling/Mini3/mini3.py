from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# 엑셀 파일 저장 이름 설정
filename = 'mini3.xlsx'

# ExcelWriter 객체 생성
writer = pd.ExcelWriter(filename, engine='xlsxwriter')

# 방문할 url(백준)
url = "https://www.acmicpc.net/"

# 크롬 드라이버의 위치 설정
driver = webdriver.Chrome('C:/chromedirver/chromedriver.exe')
driver.get(url)
time.sleep(1)

# 사이트의 위 바에서 문제 클릭
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="문제"]')))
element.click()

# 문제 탭 내의 전체 문제 클릭
driver.find_element(By.XPATH, '//a[text()="전체 문제"]').click()
time.sleep(1)

# 분류 클릭
driver.find_element(By.XPATH, '//a[text()="분류"]').click()
time.sleep(1)

# 분류 페이지의 정보 가져옴
html = driver.page_source
soup = bs(html, 'html.parser')

# tags 초기화
tags = []

# 분류 페이지에서 해당 분류의 이름과 링크를 tags에 저장
for tag in soup.select('.table > tbody > tr', limit=10):
    name = tag.select_one('a').text
    link = "https://www.acmicpc.net" + tag.select_one('a')['href']
    tags.append((name, link))


# 반복문을 돌며 정보 추출
for tag in tags:
    tag_name = tag[0] # 분류 이름
    driver.get(tag[1]) # 분류 링크로 이동
    time.sleep(1)
    html = driver.page_source # 해당 분류의 페이지 정보 가져옴
    soup = bs(html, 'html.parser')

    data=[] # 데이터 초기화

    # 문제가 너무 많아 페이지네이션 횟수를 2번으로 제한(더 많은 페이지 조회하고 싶으면 range(2)를 변경)
    for page in range(2):
        table = soup.select_one('.table-responsive') # 문제가 있는 부분 추출

        # 반복문을 돌며 문제 번호, 제목, 맞힌사람, 제출, 정답 비율, 문제 링크 추출(너무 많아서 10개로 제한)
        for row in table.select('tr', limit = 11)[1:]:
            problem_number = row.select_one('td:nth-of-type(1)').text
            problem_title = row.select_one('td:nth-of-type(2)').text.strip()
            solver = row.select_one('td:nth-of-type(4)').text
            submission = row.select_one('td:nth-of-type(5)').text
            accuracy_rate = row.select_one('td:nth-of-type(6)').text
            problem_link = 'https://www.acmicpc.net' + row.select_one('a')['href']


            # 문제 링크에 접근해서 문제 내용 추출
            driver.get(problem_link)
            time.sleep(1)
            problem_html = driver.page_source
            problem_soup = bs(problem_html, 'html.parser')
            problem_content = problem_soup.select_one('#problem_description').text.strip()

            # data에 위 추출내용 append
            data.append((tag_name, problem_number, problem_title, solver, submission, accuracy_rate, problem_link, problem_content))

        # 페이지네이션을 위해 next_page select
        next_page = soup.select_one('.pagination > li.active + li > a')
        if not next_page:
            break
        next_page_link = 'https://www.acmicpc.net' + next_page['href']
        driver.get(next_page_link) # 다음 페이지로 이동
        time.sleep(1)
        html = driver.page_source
        soup = bs(html, 'html.parser')

    # pandas를 이용하여 dataframe 생성
    df = pd.DataFrame(data, columns=['Tag', 'Problem Number', 'Problem Title','Solver', 'Submission', 'Accuracy_rate', 'Problem Link', 'Problem_Content'])
    df.index += 1 # index 1부터 시작
    df.to_excel(writer, sheet_name=tag_name, header=True, index=True, encoding='utf-8-sig') # pandas의 dataframe 객체를 excel에 저장


writer.save() # 엑셀 파일을 저장