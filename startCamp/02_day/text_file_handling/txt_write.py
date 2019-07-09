# 열기모드
# r: 읽기, w: 쓰기(write - 오버라이트), a: 추가(append)
f = open('ssafy.txt', 'w')

for i in range(10):
    f.write(f'this is line {i + 1}\n')

f.close() # open 후에는 반드시 close 한다!

with open('with_ssafy.txt', 'w') as f: # 컨텍스트 매니저
    #위드로 오픈했을때는 따로 반환값을 가질수가 없다.
    for i in range(10):
        f.write(f'this is line {i+1}\n') # 해당 블록에서 벗어나면 자동으로 close

with open('ssafy.txt', 'w', encoding='utf-8') as f:
    f.writelines(['0\n', '1\n', '2\n', '3\n']) # 여러 라인을 입력
