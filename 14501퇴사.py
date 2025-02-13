day = int(input())

# 일정표
'''
schedule = []
for _ in range(day):
    lst = list(map(int, input().split()))
    schedule.append(lst)
'''
schedule = [[3, 10], [5, 20], [1, 10], [1, 20], 
            [2, 15], [4, 40], [2, 200]]

# 남은 근무일보다 상담기간이 더 큰 날들은 빼기 
for idx, d in enumerate(schedule):
    # 남은 근무 일 = 근무일수 - 현재일자 + 1 
    left_day = day - (idx+1) + 1
    # 상담기간 
    t = d[0] 
    # 돈 
    p = d[1]
    if  left_day < t:
        schedule[idx][1] = 0 

# 돈을 버는 모든 경우의 수 구하기 
    