# requests, BeautifulSoup 패키지 가져오기
import requests
from bs4 import BeautifulSoup

# 가져올 url 문자열로 입력(네이버 정치 뉴스 페이지)
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'

# BeautifulSoup 에러로 인해 header 추가
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

# requests의 get 함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
response = requests.get(url, headers=headers)

# html을 잘 정리된 형태로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# a 태그의 class 속성명이 cluster_text_headline인 태그를 찾고 반복문을 돌며 뉴스의 text 부분만을 잘라 print
for news in soup.select('a.cluster_text_headline', limit= 10):
    print('title: ' + news.text.strip())
    print(news['href'])
