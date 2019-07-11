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

# ascii_font = requests.get(f'http://artii.herokuapp.com/fonts_list').text
# list_font = ascii_font.split('\n')
# print(list_font)
# rand_font = random.choice(list_font)
@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text')
    # Ascii Art API 를 활용해서 사용자의 input 값을 변경한다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    result = response.text
    #return text
    return render_template('ascii_result.html', result=result)


@app.route('/lotto_input')
def lotto_input():
    # 사용자가 입력할 수 있는 페이지만 전달
    return render_template('lotto_input.html')


@app.route('/lotto_result')
def lotto_result():
    lotto_round = request.args.get('round')
    lotto_numbers = request.args.get('numbers').split() # string 형태로 받아서 split() 한다
    lotto_intnum = []

    for i in range(len(lotto_numbers)):
        lotto_intnum.append(int(lotto_numbers[i]))

    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    lotto_info = response.json() # Json 타입의 파일을 python dictionary로 parsing 해줘!

    drwtNo = [lotto_info["drwtNo1"], lotto_info["drwtNo2"], lotto_info["drwtNo3"],
    lotto_info["drwtNo4"], lotto_info["drwtNo5"], lotto_info["drwtNo6"]]
    bnusNo = lotto_info["bnusNo"]

    drwt_set = set(drwtNo)
    nums_set = set(lotto_intnum)

    if len(drwt_set & nums_set) == 6:
        prize = '1등'
    elif len(drwt_set & nums_set) == 5:
        if bnusNo in lotto_intnum:
            prize = '2등'
        else:
            prize = '3등'
    elif len(drwt_set & nums_set) == 4:
        prize = '4등'
    elif len(drwt_set & nums_set) == 3:
        prize = '5등'
    else:
        prize = '낙첨'



    return f'{lotto_info["drwNo"]} 회 동행로또\n{prize} 입니다.'


if __name__ == '__main__':# 메인으로 활용할 때만 디버그 모드를 on 하겠다
    app.run(debug=True)
