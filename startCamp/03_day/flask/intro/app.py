from flask import Flask, render_template
import datetime
import random
app = Flask(__name__)

@app.route('/') # 데코레이터 : 앞에 골뱅이가 붙어있어서. 어떤 함수이다. '다음번에 설명!'
                # 하는 역할은? endpoint 루트라고 부름 route 페이지 들어갔을 때 무엇을 보여줄 것인가.
def hello():    # 함수를 만드는 방법
    # return 'Hello SSAFY!'
    return render_template('index.html') # app.py 와 같은 경로여야 함. templates파일 생성



@app.route('/ssafy')
def ssafy():
    return 'Hello SsAfY!'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    b_day = datetime.datetime(2019, 11, 11)
    td = b_day - today
    return f'{td.days} 일 남았습니다!'

@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag!</h1>'

@app.route('/html_lines')
def html_lines():
    return '''
    <h1>여러줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    '''
# Variable Routing
@app.route('/greeting/<name>') # IU
def greeting(name): # name == IU
    return render_template('greeting.html', html_name=name) # html 안으로 변수를 넘겨준다.
    # 진자2 라는 모듈이 해줌
    # render_template 라는 함수를 이용해서 templates 폴더에서 찾는다!


@app.route('/cube/<int:num>')
def cube(num):
    #num3 = num ** 3 안에서 직접 계산도 된다!
    return render_template('cube.html', html_num=num)

# 실습
@app.route('/lunch/<int:people>')
def lunch(people):
    # 사람 수 만큼의 랜덤 아이템을 menu list 에서
    # 뽑아서 보여주는 페이지!
    menu = ['짜장', '짬뽕', '볶음밥', '잡채밥', '우동']
    order = random.sample(menu, people)
    return str(order)


@app.route('/movie') # 반복문 사용
def movie():
    movies = ['스파이더맨', '엔드게임', '기생충', '알라딘']
    return render_template('movie.html', movies=movies)


if __name__ == '__main__':# 메인으로 활용할 때만 디버그 모드를 on 하겠다
    app.run(debug=True)     
# 파이썬 파일들은 모두 모듈. ex. import로 접근 가능
# 모듈이면서 우리가 실행시킬 스크립트이기도 함
# 실행 시키는 법 $ python filename.py
# 모듈을 호출하는 법
# __name__이라는 변수는 모듈로서 호출되면 '해당 모듈 이름'이라는 값을 가짐
# 직접 호출하면 '__main__'이라는 값을 가짐
