from sys import intern
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=2560x1600")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/category/MOVIE"
browser.get(url)

import time

print("프로세스 시작")
interval = 2 # 2초에 한번씩 스크롤 내림
prev_height = browser.execute_script("return document.body.scrollHeight")

print("반복 시작")
# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break

    prev_height = curr_height

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")


import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"VfPpkd-EScbFb-JIbuQc UVEnyf"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"Epkrse"}).get_text()
    
    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c P8AFK"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "          <할인되지 않은 영화는 제외>")
        continue
    
    # 할인 된 가격
    price = movie.find("span", attrs={"class":"VfPpfd VixbEe"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class":"Si6A0c ZD8Cqc"})["href"]
    # 올바른 링크 : "https://play.google.com" + link
    
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 120)

browser.quit()
