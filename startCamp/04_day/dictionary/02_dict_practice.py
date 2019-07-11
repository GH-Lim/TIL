"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
sum1 = sum(score.values())

print(f'평균 = {sum1 / len(score)} 점')




# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
avg_sum = 0
for key in scores.keys():
    sum2 = sum(scores[key].values())
    # for value in scores[key].values():
    #     sum2 = sum2 + value
    avg = sum2 / len(scores[key])
    avg_sum = avg_sum + avg
print(f'전체 평균 = {avg_sum / len(scores)} 점')





# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
for key, value in city.items():
    avg_temp = sum(value) / len(value)
    print(f'{key} : {avg_temp:.2f}')
# for key in city.keys():
#     print(f'{key} : {sum(city[key]) / len(city[key])}')








# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

city_min = {}
city_max = {}

for key in city.keys():
    city_min[key] = min(city[key])
    city_max[key] = max(city[key])

for key in city.keys():
    if min(city_min.values()) in city[key]:
        print(f'최근 3일 중 가장 추웠던 곳 : {key}')
    if max(city_max.values()) in city[key]:
        print(f'최근 3일 중 가장 더웠던 곳 : {key}')







# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.

print('==== Q3-3 ====')

if 2 in city['서울']:
    print(f'Yes\n서울은 영상 2도였던 적이 있습니다')
else:
    print(f'No\n서울은 영상 2도였던 적이 없습니다')