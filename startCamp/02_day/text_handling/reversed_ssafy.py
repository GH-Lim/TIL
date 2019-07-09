# ssafy.txt 파일을 받아 reversed_ssafy.txt로 저장
with open('ssafy.txt', 'r') as f:
    lines = f.readlines() # 각 라인을 item 으로 list 의 형태로 반환

lines.reverse() # 리스트를 역순으로 뒤집는다.

with open('reversed_ssafy.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        f.write(line)
