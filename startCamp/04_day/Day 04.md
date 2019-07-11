# Day 04

## Flask

app.py 라는 이름으로 만들면 좋다.

```python
from flask import Flask, render_template # 사용자에게 특정 html 파일을 보여줄 수 있다.
app = Flask(__name__)
```

templates 폴더는 반드시 app.py 와 같은 경로에 있어야 한다.

```python
@app.route('/') # / => root 구글의 경우에는 google.com/
def index():
    return 'Hello world!' # 사용자에게 제일 먼저 보여줄 페이지
```

```python
@app.route('/greeting/<string:name>') # variable routing 사용자의 입력값에 따라 처리
def greeting(name):					# string 이라고 명시적으로 적어주면 좋다.
    return render_template('greeting.html', name=name)
# html 파일로 name 이라는 변수를 넘겨준다
```

```html
<!DOCTYPE html> /!-- '!+tab'을 하면 html 양식이 나온다 --/
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>greeting</title>
</head>
<body>
    <h1>Hi, {{name}} !</h1> <!-- {{}} 수염모양 안쪽에 받아온 변수 입력 -->
</body>
</html>
```

```python
if __name__ == '__main__':# 메인으로 활용할 때만 디버그 모드를 on 하겠다
    app.run(debug=True)
```



### 사용자 정보 받기

로그인 창을 보여달라는 요청 /

로그인 창을 보여주는 페이지 / 로그인을 해달라는 요청

2가지가 필요하다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Ping</title>
</head>
<body>
    <!-- action 은 form 을 보내는 url 을 정의하는 곳 -->
    <form action="/pong"> <!-- pong으로 보내라 -->
        <input type="text" name="age"> <!--  -->
        <button type="submit">제출하기</button> <!-- 버튼 타입 지정 -->
    </form>
    <!-- form 태그 안쪽에 작성해야 한다. -->
</body>
</html>
```

사용자가 보낸 요청을 확인할 수 있는 flask의 객체 request

```python
from flask import Flask, render_template, request

@app.route('/pong')
def pong():
    age = request.args.get('age') # 사용자가 보낸 입력값을 age로 받는다
    # return render_template('pong.html')
    return f'Pong! age: {age}'
```

### API 연습

ASCII Art 를 이용

사용자에게 입력을 요청 - 입력 받은 값을 저장

API에게 font list를 요청 받아 랜덤하게 뽑는다.

API에게 make 요청을 보낸다

사용자에게 다시 보여준다!