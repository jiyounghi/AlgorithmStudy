num1, num2 = map(int, input().split())
win = 0 # 이기는 경우

# 전체 경우의 수 
total = (18 * 17) // 2

# 영학이가 이기는 경우 계산 
if num1 == num2 :
    win = 10 + (num1 -1)
else :
    win = (num1 + num2) % 10 
    
print(f'{win/total:.3f}')
    