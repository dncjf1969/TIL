#플라스크 실행하려면 무조건 파일이름을 app.py로 해야한다.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# 127.0.0.1:5000/ssafy로 주소입력 했을 때
@app.route('/ssafy')
# 함수 ssafy를 작성하고
def ssafy():
    # hello ssafy라는 내용을 반환하는 결과를 만들어보자
    return "upipupipupipipipipipipipipipi!!!"














if __name__ == '__main__':
    app.run(debug=True)