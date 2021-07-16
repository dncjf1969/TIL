#setWebHook 요청 보내야 한다.
import requests
from requests.models import Response

#token, url, ngrok url
TOKEN = '1742350070:AAE77_rDFiFU7hCO1qfXFtx2xPjSa-neA7Y'
url = f'https://api.telegram.org/bot{TOKEN}'
ngrok_url = 'https://32a4d53906cf.ngrok.io'
python_anywhere = 'https://dncjf1969.pythonanywhere.com'
set_webhook_url = f'{url}/setWebhook?url={python_anywhere}/telegram'
# telegram이 내 ngrok/telegram으로 요청을 보내고 200 응답 받아간다.

response = requests.get(set_webhook_url)
print(response.text)