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

    drwtNo = []
    for i in range(1, 7):
        drwtNo.append(lotto_info[f'drwtNo{i}']) # f_string을 이용하여 for문으로
    # drwtNo.append(str(lotto_info[f'drwtNo{i}'])) str로 비교하려 할 경우 이렇게 할 수 있다!

    # drwtNo = [lotto_info["drwtNo1"], lotto_info["drwtNo2"], lotto_info["drwtNo3"],
    # lotto_info["drwtNo4"], lotto_info["drwtNo5"], lotto_info["drwtNo6"]]
    bnusNo = lotto_info["bnusNo"]

    drwt_set = set(drwtNo)              # 당첨번호
    nums_set = set(lotto_intnum)        # 사용자입력번호
    samenum = list(drwt_set & nums_set) # 교집합
    

    if len(lotto_intnum) == 6:          # 사용자가 보낸 번호가 올바른지 확인 (6개가 맞는지)

        if len(samenum) == 6:
            prize = '1등'
        elif len(samenum) == 5:
            if bnusNo in lotto_intnum:
                prize = '2등'
                samenum.append(bnusNo)
            else:
                prize = '3등'
        elif len(samenum) == 4:
            prize = '4등'
        elif len(samenum) == 3:
            prize = '5등'
        else:
            prize = '낙첨'

        # matched = 0
        # for number in lotto_numbers:
        #   if number in winner:
        #       matched += 1            # 당첨시 matched 를 1씩 증가 시킨다.
        # 
    else:
        prize = '올바르지 않은 번호'
        samenum = []

    samenum.sort()
    drwtNo.sort()
    lotto_intnum.sort()

    return render_template('lotto_result.html', lotto_round=lotto_round, prize=prize, samenum=samenum,
    bnusNo=bnusNo, drwtNo=drwtNo, lotto_intnum=lotto_intnum)
#    return f'{lotto_info["drwNo"]} 회 동행로또\n{prize} 입니다.'


if __name__ == '__main__':# 메인으로 활용할 때만 디버그 모드를 on 하겠다
    app.run(debug=True)
