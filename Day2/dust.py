import requests
from bs4 import BeautifulSoup

key = 'hqHreUgAGaNDQhvOq5W%2BjUmmcr3GO2sBDwZMfU5HfBOijhu%2BCk3pKIwWn%2FxKh1rgilR91eZplTZkU3CoaGEXLw%3D%3D'
sidoName = input('전국, 서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종 중에서 선택해주세요 :')
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType=json&numOfRows=100&pageNo=1&sidoName={sidoName}&ver=1.0'

response = requests.get(url).json()
# print(response)

# sido_name = response['response']['body']['items'][1]['sidoName']
# station_name = response['response']['body']['items'][1]['stationName']
# dust = response['response']['body']['items'][1]['pm10Value']
# # print(f'{sido_name}시 {station_name}의 미세먼지 농도는 {dust}입니다.')

station_user_input = input('동 명을 입력해 주세요 : ')
items = response['response']['body']['items']
for value in items :
    if value['stationName'] == station_user_input:
        sido_name = value['sidoName']
        station_name = value['stationName']
        dust = value['pm10Value']
print(f'{sido_name}시 {station_name}의 미세먼지 농도는 {dust}입니다.')
