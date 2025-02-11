def bnp(initial_cash, prices):
    cash = initial_cash
    stocks = 0

    for price in prices:
        if cash >= price:
            stocks += cash // price
            cash %= price

    return cash + stocks * prices[-1]

def timing(initial_cash, prices):
    cash = initial_cash
    stocks = 0

    for i in range(3, len(prices)):
        if prices[i-3] < prices[i-2] < prices[i-1] < prices[i]:  # 3일 연속 상승
            cash += stocks * prices[i]
            stocks = 0
        elif prices[i-3] > prices[i-2] > prices[i-1] > prices[i]:  # 3일 연속 하락
            if cash >= prices[i]:
                stocks += cash // prices[i]
                cash %= prices[i]

    return cash + stocks * prices[-1]

# 입력 처리
initial_cash = int(input())
prices = list(map(int, input().split()))

# 전략 실행
bnp_result = bnp(initial_cash, prices)
timing_result = timing(initial_cash, prices)

# 결과 출력
if bnp_result > timing_result:
    print("BNP")
elif bnp_result < timing_result:
    print("TIMING")
else:
    print("SAMESAME")
