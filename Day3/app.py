#Flask 불러온다.
#Flask는 파이썬이 기본으로 가지고 있는 모듈이 아니다.
#그럼 설치해야한다.
#설치는 pip라고 하는 파이썬 패키지 관지를 통해서 한다.
#pip install Flask -> bash창에 입력해서 설치한다.

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

TOKEN = '1742350070:AAE77_rDFiFU7hCO1qfXFtx2xPjSa-neA7Y'
 # 요청 통합 URL 변수에 담기
url = f'https://api.telegram.org/bot{TOKEN}'
#메세지 보낼 사람 chat_id 필요
chat_id = 1724719735

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# /ssafy -> hello, SSAFY
# Flask로 어떤 문서를 응답할 때, return에 작성하는 것이 아니라
# 특정 문서 자체를 불러와서 응답해줄 수 있다.
# render_template
# flask가 가지고 있는 함수 render_template을 불러와야 한다.

@app.route('/ssafy')
def ssafy():
    #ssafy.html을 rendering 한다.
    return render_template('ssafy.html')

    
# #로그인이든 아니든 채팅이든
# 내가 입력한 값을 보낼 수 있는 
# 메시지를 보낼 수 있고, 보내온 메시지를 받아서 어떤 행위를 실행하는 코드를 작성
# 함수가 2개 필요하다.

# write함수(메시지를 입력하는 곳), send(메시지를 받는 곳)
# 주소 함수이름이랑 동일하게 작성한다.
# html 이름도 함수 이름이랑 동일하게 작성한다.
# 안의 내용은 일단은 제목만 입력해서 
# 두 페이지 정상 작동하는지 확인
@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    # print(request)
    # print(dir(request))
    message = request.args.get('message')
    print(message)

    #텔레그램 챗봇 api url 필요
    #내 챗봇 토큰 필요
    send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={message}'
    #파이썬으로 요청보내는 requests 필요
    requests.get(send_message_url)
    return render_template('send.html')

# POST 방식의 요청만 받겠다.
@app.route('/telegram', methods=['POST'])
def telegram():
    # 요청 정보는 request에 들어있다.
    response = request.get_json()
    print(response)

    #1
    #사용자가 챗봇한테 보낸 메세지 똑같이 돌려보내주는 코드
    #2
    #text에 들어있는 값이 '누구야' 일때
    #저는 ~~님의 챗봇입니다.

    chat_id = response['message']['from']['id']
    text = response['message']['text']
    if text == "누구야?" :
        text = "저는 이우철님의 챗봇입니다."

    #3
    # 미세먼지 API코드 가지고 와서 '미세먼지' 라고 입력받으면
    # 미세먼지 정보를 알려주는 코드 
    # 사용자가 보내온 메시지가 '미세먼지' 일때만,
    elif text == '미세먼지':
        key = 'hqHreUgAGaNDQhvOq5W%2BjUmmcr3GO2sBDwZMfU5HfBOijhu%2BCk3pKIwWn%2FxKh1rgilR91eZplTZkU3CoaGEXLw%3D%3D'
        sidoName = '부산'
        dust_url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType=json&numOfRows=100&pageNo=1&sidoName={sidoName}&ver=1.0'
        response = requests.get(dust_url).json()
        # print(response)

        sido_name = response['response']['body']['items'][1]['sidoName']
        station_name = response['response']['body']['items'][1]['stationName']
        dust = response['response']['body']['items'][1]['pm10Value']
        text = (f'{sido_name}시 {station_name}의 미세먼지 농도는 {dust}입니다.')

    send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(send_message_url).json()

    # 응답은 본문과 status_code 200을 같이 보내준다.
    return '', 200





#debug mode : on
if __name__ == '__main__':
    app.run(debug=True)