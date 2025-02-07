from itertools import combinations

# 입력 받기
num1, num2 = map(int, input().split())

# 전체 경우의 수
total = (18 * 17) // 2  # 정수 나눗셈

# 모든 가능한 상대 패 조합 만들기
cards = []
for i in range(1, 11):
    cards.append(i)
    cards.append(i)
cards.remove(num1)
cards.remove(num2)

# 영학이의 족보 계산
def get_rank(a, b):
    if a == b:
        return (10, a)  # 땡 족보 (큰 값이 유리)
    return (0, (a + b) % 10)  # 끗 족보 (합의 일의 자리)

my_rank = get_rank(num1, num2)

win = 0  # 이기는 경우의 수

# 상대방이 가져갈 수 있는 모든 경우 비교
for opp1, opp2 in combinations(cards, 2):
    opp_rank = get_rank(opp1, opp2)
    if my_rank > opp_rank:
        win += 1

# 확률 계산 및 출력
print(f"{win/total:.3f}")
