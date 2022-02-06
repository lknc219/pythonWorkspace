import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

res =requests.get(url, headers=headers)
res.raise_for_status() # 응답코드가 정상이면 코드실행, 에러코드이면 실행 종료

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)