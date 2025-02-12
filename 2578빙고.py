# 철수의 빙고판 
'''
bingo = []
for _ in range(5):
    lst = list(map(int, input().split()))
    bingo.append(lst)
print(bingo)
'''
bingo = [[11, 12, 2, 24, 10], [16, 1, 13, 3, 25], 
         [6, 20, 5, 21, 17], [19, 4, 8, 14, 9], 
         [22, 15, 7, 23, 18]]


# 사회자가 부르는 수 
'''
num = []
for _ in range(5):
    lst = list(map(int, input().split()))
    num.append(lst)
print(num)
'''
num = [5, 10, 7, 16, 2, 4, 22, 8, 17, 13, 
       3, 18, 1, 6, 25, 12, 19, 23, 14, 21, 
       11, 24, 9, 20, 15]

# 선의 개수
cnt = 0

def make_line(bingo):
    
    cnt = 0 
    
    # 가로선 확인
    for row in bingo:
        if row.count(0) == 5:  # 한 줄이 모두 0이면 빙고
            cnt += 1

    # 세로선 확인
    for col in range(5):
        if all(bingo[row][col] == 0 for row in range(5)):  # 한 열이 모두 0이면 빙고
            cnt += 1

    # 대각선 확인 (왼쪽 위 → 오른쪽 아래)
    if all(bingo[i][i] == 0 for i in range(5)):
        cnt += 1

    # 대각선 확인 (오른쪽 위 → 왼쪽 아래)
    if all(bingo[i][4 - i] == 0 for i in range(5)):
        cnt += 1

    return cnt
        
    
# 사회자가 부르는 수를 차례로 확인하며 빙고 체크
idx = 0
while idx < len(num):
    n = num[idx]
    idx += 1  # 몇 번째 숫자인지 직접 관리

    for i in range(5):
        if n in bingo[i]:  # 숫자가 있으면
            j = bingo[i].index(n)
            bingo[i][j] = 0  # 0으로 변경

            if make_line(bingo) >= 3:  # 빙고 3줄 이상이면 종료
                print(idx)  # 몇 번째 숫자에서 빙고가 완성되는지 출력
                exit()