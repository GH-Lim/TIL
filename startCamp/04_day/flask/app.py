from flask import Flask, render_template, request
app = Flask(__name__)
import requests
import random
#from bs4 import BeautifulSoup


@app.route('/') # / => root
def index():
    return 'Hello world!'

@app.route('/greeting/<string:name>') # variable routing
def greeting(name):
    return render_template('greeting.html', name=name)


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    age = request.args.get('age') # 사용자가 보낸 입력값을 age로 받는다
    # return render_template('pong.html')
    return f'Pong! age: {age}'


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/naver')
def naver():
    return render_template('naver.html')

# 사용자가 입력할 수 있는 페이지 만들기
@app.route('/ascii_input')
def ascii_input():
    return render_template('ascii_input.html')

ascii_font = requests.get(f'http://artii.herokuapp.com/fonts_list').text
list_font = ascii_font.split('\n')
#print(list_font)
rand_font = random.choice(list_font)
@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text')
    # Ascii Art API 를 활용해서 사용자의 input 값을 변경한다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={rand_font}')
    result = response.text
    #return text
    return render_template('ascii_result.html', result=result)


if __name__ == '__main__':# 메인으로 활용할 때만 디버그 모드를 on 하겠다
    app.run(debug=True)
