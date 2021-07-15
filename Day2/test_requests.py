#파이썬으로 요청 보내기 위한 준비
#requests라는 모듈을 사용할 거다.
import requests

#requests로 https://www.naver.com으로 요청 보낸 결과 출력
print(requests.get('http://www.naver.com'))
print(requests.get('http://www.naver.com').text)
print(requests.get('http://www.naver.com').status_code)