import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%A3%A8%EB%82%98%EB%9E%A9+%EC%B1%85%EC%83%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

items = soup.find_all("li", attrs={"class": re.compile("^search-product")}) 
# print(items[0].find("div", attrs={"class":"name"}).get_text())
for item in items:

    # 광고 제품은 제외한다
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("         <광고 상품은 제외합니다.")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
    
    # 어린이 제품 제외
    if "어린이" in name:
        print("         <어린이 상품 제외힙니다.")
        continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text()# 가격

    # 리뷰 50개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"})#평점
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"
        print("         <평점 없는 상품 제외합니다.")
        continue

    rate_count = item.find("span", attrs={"class":"rating-total-count"}) # 평점 수
    if rate_count:
        rate_count = rate_count.get_text()
        rate_count = rate_count[1:-1]
    else:
        rate_count = "평점 수 없음"
        print("         <평점 수 없는 상품 제외합니다.")
        continue

    if float(rate) >= 4.5 and int(rate_count) >= 50:
        print(name, price, rate, rate_count)
    