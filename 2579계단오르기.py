import sys

# 입력 처리
n = int(sys.stdin.readline().strip())
stairs = [0] * (n + 1)

for i in range(1, n + 1):
    stairs[i] = int(sys.stdin.readline().strip())

# 예외 처리 (계단이 1개 또는 2개만 있는 경우)
if n == 1:
    print(stairs[1])
elif n == 2:
    print(stairs[1] + stairs[2])
else:
    # DP 배열 초기화
    dp = [0] * (n + 1)
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

    # 점화식을 이용한 DP 채우기
    for i in range(4, n + 1):
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

    # 최댓값 출력
    print(dp[n])
