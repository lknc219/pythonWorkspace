import requests
res = requests.get("http://google.com")
# res =requests.get("http://nadocoding.tistory.com")
res.raise_for_status() # 응답코드가 정상이면 코드실행, 에러코드이면 실행 종료

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)