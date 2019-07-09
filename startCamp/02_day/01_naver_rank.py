import requests
import bs4

url = 'https://www.naver.com/' # 아이디는 #으로 접근 / 클래스는 .으로 접근

selector = '.ah_k'

response = requests.get(url)

html = response.text

soup = bs4.BeautifulSoup(html, 'html.parser')

ranks = soup.select(selector) # '.ah_l .ah_item .ah_a .ah_k' 이 부분만 셀렉트하는 셀렉터

#print(rank)

for rank in ranks:
    print(rank.text)
    #print('%d위 %s'%(i+1, rank[i].text))

