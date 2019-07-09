import requests # requests 모듈을 사용하기 위해 불러옴 해당 url에 요청을 보냄
import bs4 # Beautiful Soup HTML파일에 접근 가능하고 싶은 형태로 바꿔줌.

url = 'https://finance.naver.com/sise/' # 이 주소로 들어가서 코스피 정보를 가져오고싶다

response = requests.get(url) # response.text
html = response.text

print(response)
print(response.status_code)

soup = bs4.BeautifulSoup(html, 'html.parser') # 파싱?
kospi = soup.select_one('#KOSPI_now').text # 파싱을 했기 때문에 셀렉트 원으로 접근 가능
# 아이디로 접근할땐 #으로 접근

#KOSPI_now

print(kospi)
