import requests # 1. Bithumb 페이지를 가지고 온다
import bs4
#import csv

url = 'https://www.bithumb.com/' # 빗썸 url

selector = '.coin_list tr td:nth-child(1) strong'#'#tableAsset tbody tr td p a strong'
selector2 = '.coin_list tr td:nth-child(2) strong'

response = requests.get(url) # 요청을 보내 응답을 받는다.
#response [200] 응답코드 200 잘 받았다.
html = response.text # 응답 받은 객체에서 html 문서를 string으로 가져온다.

soup = bs4.BeautifulSoup(html, 'html.parser')
# 2. Beautiful Soup 모듈을 이용하여 string type 의 html 을 파싱한다@

coins = soup.select(selector) # '.ah_l .ah_item .ah_a .ah_k' 이 부분만 셀렉트하는 셀렉터
vals = soup.select(selector2) # a.replace(',','')

#coin_info = {'코인명' : '가격'}

# print(len(coins),len(vals))

with open('coin_info.csv', 'w', encoding='utf-8') as f:
     for i in range(len(coins)):
         coin = coins[i].text.rstrip('NEW').strip()
         val = vals[i].text.replace(',','').rstrip('원')
         val = float(val) # 숫자로 저장
         f.write(f'{coin},{val}\n')

# for i in range(len(coins)):
#     coin_info[coins[i].text.rstrip('NEW').strip()] = vals[i].text.replace(',','').rstrip('원')
# 코인 이름 중 'NEW' 제거 후 양쪽 공백 제거
# 코인 가격 중 ',' 제거 후 '원' 제거

# with open('coin_info.csv', 'w', encoding='utf-8', newline='') as f: 
#     csv_writer = csv.writer(f) # f 라는 파일에 csv 를 작성하는 개체를 생성
#     for item in coin_info.items():
#         csv_writer.writerow(item)
