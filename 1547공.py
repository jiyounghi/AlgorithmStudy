M = int(input())  # 교환 횟수 입력
cup= [1, 2, 3]
for _ in range(M):
    x, y = map(int, input().split())
    cup[cup.index(x)], cup[cup.index(y)] = cup[cup.index(y)], cup[cup.index(x)]
    print(cup)

print(cup[0])  # 최종적으로 공이 있는 위치 출력