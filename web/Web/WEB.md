# WEB

## HTML

get: 주세요 => 요청한 정보를 줌, post: 해주세요 => 했음

남의 컴퓨터 주소/dir1/dir2/../WantThis.file

남의 컴퓨터가 가지고 있는 file을 줘라

### IP(Internet Protocol)

`172.217.27.78`

8비트(0~255)까지의 숫자로 구성된 숫자의 집합으로, 각자가 가지고 있는 주소와 동일하다.

### 도메인

`google.com`

네트워크상의 컴퓨터를 식별하는 호스트명

### URL(Uniform Resource Locator)

`https://www.google.co.kr/search?q=구글`

도메인 + 경로, 실제로 해당 서버에 저장된 자료의 위치

## Static web

매번 똑같은 페이지를 사용자에게 제공함

만들어놓고 파는 것

스태틱웹이 좋다? 좋을수도 아닐수도

URL(파일식별자)은 **네트워크 상에서 자원이 어디 있는지를 알려주기 위한** 고유 규약이다

흔히 웹 사이트 주소로 알고 있지만, URL은 웹 사이트 주소 뿐만 아니라

컴퓨터 네트워크 상의 자원을 모두 나타낼 수 있다

URI(통합자원식별자)는 **인터넷에 있는 자원을 나타내는** 유일한 주소이다.

URI의 하위 개념으로 URL, URN이 있다.

URL : `www.google.com/logo.jpg` => 구글로고 사진

URI : `www.google.com/search?q=파이썬` => 구글이 가지고 있는 자원

## HTML

### Hyper Text Markup Language

### Hyper Text

종이책: 흐름대로 읽도록 구성, 

하이퍼텍스트: 하나의 문서에서 다른 문서로 가는 경로가 여러개 있다.

- Hyper Text를 주고받는 규칙 : Transfer Protocol => HTTP
- 웹 펭지를 작성하기 위한 역할 표시 언어

HTML 파일: HTML로 작성된 문서파일

## CSS(Cascading Style Sheet)

꾸며주는 역할 내일 더 다루도록 합니다.

## JavaScript

웹 표준 HTML Living Standard (WHATWG)

1. HTML 문서의 기본 구조

   DOCTYPE 선언부

   html 요소 (head 와 body 부분으로 구분된다.)

   ```html
   <!DOCTYPE html>
   <html lang="ko">
   <head>
     <meta charset="UTF-8">
     <title>Document</title>
   </head>
   <body>
           
   </body>
   </html>
   ```

   속성값은 붙여쓰고 쌍따옴표로 적는다. `lang="ko"`

   태그 안에메타태그 클로징 태그가 없다 셀프클로징을 명시적으로 작성한다. < />

2. Tag와 DOM TREE(Document Object Model)

   0. 주석(comment)

      `<!--주석 내용-->`

   1. 요소(Element)

      `<h1>contents</h1>`

      태그와 내용으로 구성되어 있다.

      요소안에 요소 중첩 가능

   2. Self-closing element

      `<img src="url" />` `<br/>`개행문자

      HTML은 에러를 내지 않는다.

   3. 속성(Attribute)

      `<a href="https://google,com"></a>`

      공백 no " "사용

   4. DOM 트리

   5. 시맨틱 태그(Semantic Tag)

      `<div></div>` non semantic 요소

      공간을 분할할 뿐 의미는 없다.

      시맨틱 : 의미 있는 정보의 그룹을 태그로 표현하여 단순히 보여주기 위한 것을 넘어서 의미를 가지는 태그들을 활용하기 위한 노력

## 검색엔진 최적화(SEO)

수업에서 다루진 않음

## semantic_html

`&lt;header&gt;` <> 를 표현하는 법

