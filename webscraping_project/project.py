from re import U
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def create_soup(url, headers):
    if headers:
        res = requests.get(url, headers=headers)
    else:
        res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

# 네이버 기상정보 가져오기
def scrape_weather():
    # 스크래핑 사이트 정보
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B2%BD%EA%B8%B0%EB%8F%84+%EA%B4%91%EC%A3%BC+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hQ9BdwprvTossnbnho0ssssstrC-267741"
    headers = {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
    soup = create_soup(url, headers)
    
    # 어제보다 5도 높아요 맑음
    cast = soup.find("p", attrs={"class":"summary"}).get_text()
    
    # 현재온도 최저온도 최고온도
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().strip()
    temp = soup.find("span", attrs={"class":"temperature_inner"}).get_text().split("/")
    min_temp = temp[0].strip()
    max_temp = temp[1].strip()  
    
    # 강수확률 습도 바람
    dl_lst = soup.find("dl", attrs={"class":"summary_list"})
    dt_lst = dl_lst.find_all("dt")
    dd_lst = dl_lst.find_all("dd")
    rain_rate = dt_lst[0].get_text() + " " + dd_lst[0].get_text()
    humidity = dt_lst[1].get_text() + " " + dd_lst[1].get_text()
    wind = dt_lst[2].get_text() + " " + dd_lst[2].get_text()
    
    # 미세먼지 초미세먼지 상태
    to_chart_list = soup.find("ul", attrs={"class":"today_chart_list"})
    fine_dust = to_chart_list.find_all("li")[0].get_text().strip()
    ultra_fine_dust = to_chart_list.find_all("li")[1].get_text().strip()

    # 출력
    print("[오늘의 날씨]")
    print(cast)
    print("{0} ({1} / {2})".format(curr_temp, min_temp, max_temp))
    print("{0} / {1} / {2}".format(rain_rate, humidity, wind))
    print("{0} / {1}".format(fine_dust, ultra_fine_dust))

# 네이버 언론사별 가장 많이 본 뉴스 5개 가져오기
def scrape_headline_news():
    print("[언론사별 가장 많이 본 뉴스]")
    # 스크래핑 사이트 정보
    url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
    headers = {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
    soup = create_soup(url, headers)

    # soup = create_soup(url, headers)
    # with open("project_test.html", "w" ,encoding="utf-8") as f:
    #     f.write(soup.prettify())
    # 언론사별 가장 많이 본 뉴스 목록
    # head_lines = soup.find("ul", attrs={"class":"section_list_ranking_press _rankingList"}).find_all("li", limit=3)
    # print("head_lines의 size ::: ", head_lines.count)
    # for news in head_lines:
    #     tag_a = news.find("a", attrs={"class":"list_tit nclicks('rig.renws2')"})
    #     title = tag_a.get_text()
    #     link = tag_a["href"]
    #     print(title)
    #     print(link)



    #출력


if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기
    # scrape_headline_news()
    # it 뉴스3개
    # 영어회화 한줄