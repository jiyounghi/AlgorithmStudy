def make_one(n):
    dp = [0] * (n + 1)  # dp 테이블 초기화 (0부터 n까지)

    for i in range(2, n + 1):
        # 기본적으로 1을 빼는 연산
        dp[i] = dp[i - 1] + 1

        # 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        # 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]

# 입력값 처리
n = int(input().strip())
print(make_one(n))