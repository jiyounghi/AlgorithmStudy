M = int(input())  # 교환 횟수 입력
ball = 1  # 처음 공이 있는 위치

for _ in range(M):
    X, Y = map(int, input().split())  # X번 컵과 Y번 컵을 교환
    if ball == X:
        ball = Y  # 공이 X에 있으면 Y로 이동
    elif ball == Y:
        ball = X  # 공이 Y에 있으면 X로 이동

print(ball)  # 최종적으로 공이 있는 위치 출력