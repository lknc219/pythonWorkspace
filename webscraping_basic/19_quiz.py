# Quiz) ssg에서 루나랩 책상에 대한 정보를 스크래핑하는 프로그램을 만드시오

# [조회 조건]
# 1. http://www.ssg.com/ 접속
# 2. '루나랩 모션데스크' 검색
# 3. 결과 정보 출력 (80만원 이하)

# [출력 결과]
# ============ 상품 1 ============
# 이름   : 
# 가격   : 
# 별점   : 
# 별점수 : 
# 판매자 : 
# 링크   : 
# ============ 상품 2 ============
#     ...

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

browser = webdriver.Chrome()

url = "http://www.ssg.com/"

browser.get(url)

browser.find_element_by_id("ssg-query").send_keys("루나랩 모션데스크")
browser.find_element_by_id("ssg-query").send_keys(Keys.ENTER)

soup = BeautifulSoup(browser.page_source, "lxml")

items = soup.find_all("li", attrs={"class":"cunit_t232"})
with open("desk_price.txt", "w", encoding="utf8") as f:
    for idx, item in enumerate(items):
        
        if int(item.find("em", attrs={"class":"ssg_price"}).get_text().replace(",","")) > 500000:
            continue
        title_div = item.find("div", attrs={"class":"title"})
        title_div_a = title_div.find("a", attrs={"class":"clickable"})

        name = title_div_a.find("em", attrs={"class":"tx_ko"}).get_text()
        price = item.find("em", attrs={"class":"ssg_price"}).get_text()
        rating = item.find("div", attrs={"class":"rating"})
        if rating:
            rate = rating.find("span", attrs={"class":"blind"}).get_text()
            rate_cnt = rating.find("span", attrs={"class":"rate_tx"}).find("em").get_text()
        else:
            rate = "별점 없음"
            rate_cnt = "별점 수 없음"
        seller = title_div.find("strong", attrs={"class":"brd"})
        if seller:
            seller = seller.find("em", attrs={"class":"tx_ko"}).get_text()
        else:
            seller = "판매자정보 없음"
        link = "http://www.ssg.com" + title_div_a["href"].replace(" ","%20")

        
        f.writelines("==================================== 상품 {0} ====================================\n".format(idx+1))
        f.writelines(f"이름 \t: {name}\n")
        f.writelines(f"가격 \t: {price}\n")
        f.writelines(f"별점 \t: {rate}\n")
        f.writelines(f"별점수 \t: {rate_cnt}\n")
        f.writelines(f"판매자 \t: {seller}\n")
        f.writelines(f"링크 \t: {link}\n\n")

        print("============ 상품 {0} ============".format(idx+1))
        print(f"이름 \t: {name}")
        print(f"가격 \t: {price}")
        print(f"별점 \t: {rate}")
        print(f"별점수 \t: {rate_cnt}")
        print(f"판매자 \t: {seller}")
        print(f"링크 \t: {link}")
    
browser.quit()