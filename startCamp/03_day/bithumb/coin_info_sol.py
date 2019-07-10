import requests # 1. Bithumb 페이지를 가지고 온다
import bs4
import csv

url = 'https://www.bithumb.com/' # 빗썸 url

response = requests.get(url) # 요청을 보내 응답을 받는다.
#response [200] 응답코드 200 잘 받았다.
html = response.text # 응답 받은 객체에서 html 문서를 string으로 가져온다.

soup = bs4.BeautifulSoup(html, 'html.parser')
# 2. Beautiful Soup 모듈을 이용하여 string type 의 html 을 파싱한다@
# HTML을 스트링으로 가져온 것을 BS를 이용하여 의미있는 파일로 만듦

# 3. 각 코인의 정보가 담겨있는 table row 데이터를 list 의 형태로 가져온다.
coins = soup.select('.coin_list tr') # 태그니까 태그 이름
# print(coins) 출력을 해보니 리스트[]로 잘 가져와졌다.


# 5. csv writer 를 이용해서 정보를 저장한다.
with open('coin_info_sol.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)

    # 4. 각 코인을 순회하며 필요한 정보만 추출한다.
    for coin in coins:
        coin_name = coin.select_one('td:nth-child(1) > p > a > strong').text.replace('NEW','').strip()
        coin_price = coin.select_one('td:nth-child(2) > strong').text
        data = (coin_name, coin_price)
        
        csv_writer.writerow(data)
        #tableAsset > tbody > tr:nth-child(1) > td:nth-child(1)
        # '>' 와 ' '의 차이 : '>' 는 바로 다음
        # print(coin_name, coin_price)