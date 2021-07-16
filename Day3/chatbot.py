#requests 불러오기
import requests
from pprint import pprint

# 봇 토큰 변수에 담기
TOKEN = '1742350070:AAE77_rDFiFU7hCO1qfXFtx2xPjSa-neA7Y'
# 요청 통합 URL 변수에 담기
url = f'https://api.telegram.org/bot{TOKEN}'
# print(url)

# 내 챗봇에 메세지 보낸 사람 정보 알아내기
get_updates_url = f'{url}/getUpdates'
print(get_updates_url)
response = requests.get(get_updates_url).json()
# 그 사람이 보낸 메세지와, 그 사람의 chat_id 알아내기
chat_id = response['result'][0]['message']['from']['id']
text = response['result'][0]['message']['text']
# pprint(response)
print(chat_id, text)
# 메세지 보낸 사람에게
# 그 사람이 보낸 메세지 다시 돌려보내기
send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(send_message_url).json()