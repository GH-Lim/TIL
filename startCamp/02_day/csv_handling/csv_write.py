dinner = {
    '양자강': '02-557-4211', # 차돌짬뽕
    '김밥카페': '02-553-3181', # 라돈
    '순남시레기': '02-508-0887' # 보쌈정식
}
# dinner.keys() # 키 값만 가져온다.
# dinner.values() # 밸류 값만 가져온다.

# 1. String formatting
with open('dinner.csv', 'w', encoding="utf-8") as f:
    for item in dinner.items(): # [['양자강','02-557-4211'],[김밥카페, '...'], ...] 키, 밸류 둘 다 가져옴
        f.write(f'{item[0]},{item[1]}\n') # 양자강,02-557-4221

# 2. csv writer
import csv

with open('dinner.csv', 'w', encoding='utf-8', newline='') as f: # window 환경에서는 개행\n이 추가로 된다
    # newline=''로 빈칸으로 만든다. # 옵션에는 = 사이에 공백 없이
    csv_writer = csv.writer(f) # f 라는 파일에 csv 를 작성하는 개체를 생성
    for item in dinner.items():
        csv_writer.writerow(item)
