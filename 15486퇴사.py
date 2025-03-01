import sys

# 입력 받기
N = int(sys.stdin.readline().strip())
schedule = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# DP 배열 초기화
dp = [0] * (N + 1)

# DP 업데이트
for i in range(N):
    Ti, Pi = schedule[i]
    
    # 상담을 하지 않는 경우 (현재까지의 최대 수익 유지)
    if i > 0:
        dp[i] = max(dp[i], dp[i - 1])
    
    # 상담을 하는 경우 (i + Ti일에 상담 완료)
    if i + Ti <= N:
        dp[i + Ti] = max(dp[i + Ti], dp[i] + Pi)

# 결과 출력
print(max(dp))
