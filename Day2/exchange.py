
# requests, bs4를 불러온다.
# 요청보내기위한 url
# 위 url로 요청을 보낸다
# 응답받은 문서를 파이썬이 읽을 수 있게 변환한다
# 변환 후, 내가 원하는 정보 부분만 선택한다.
# 선택한 정보 중에 텍스트만 뽑는다. 
# 출력한다


import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
data = BeautifulSoup(response,'html.parser')
exchange = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
print(exchange)

result = exchange.text
print(f'현재 원/달러의 환율은 {result}입니다.')