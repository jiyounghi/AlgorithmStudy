M = int(input())  # 교환 횟수 입력
cup= [1, 2, 3]
for _ in range(M):
    x, y = map(int, input().split())
    c1 = cup.index(x)
    c2 = cup.index(y)
    cup[c1], cup[c2] = cup[c2], cup[c1]

print(cup[0])  # 최종적으로 공이 있는 위치 출력