from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)

# 가는 날 선택 클릭
# browser.find_element_by_link_text("가는날 선택") # 강의내용
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

# 이번달 ?일, ?일 선택
browser.find_elements_by_link_text("5")[0].click() #[0] -> 27의 text를 지닌 element중 첫번째 
browser.find_elements_by_link_text("6")[0].click() #[0] -> 28의 text를 지닌 element중 첫번째

# 제주도 선택
browser.find_element_by_xpath("~~").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "xpath값")))
    # 성공했을 때 동작
    print(elem.text) # 첫번째 결과 출력
finally:
    browser.quit()

# 첫번째 결과 출력
# elem = browser.find_element_by_xpath("!!")
# print(elem.text)
