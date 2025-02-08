# 입력 받기
N, M = map(int, input().split())  

arr = []
for _ in range(N):
    line = input().strip()        
    char_list = list(line)        
    int_list = list(map(int, char_list)) 
    arr.append(int_list) 

max_size = 1  # 최소 정사각형 크기 (1x1)

# 가능한 최대 변 길이
max_len = min(N, M)

# 변의 길이를 1부터 최대 길이까지 시도
for length in range(1, max_len + 1):  
    for i in range(N - length):       # 왼쪽 위 꼭짓점의 행 좌표
        for j in range(M - length):   # 왼쪽 위 꼭짓점의 열 좌표
            # 네 꼭짓점이 같은 숫자인지 확인
            if (arr[i][j] == arr[i + length][j] == arr[i][j + length] == arr[i + length][j + length]):
                max_size = (length + 1) ** 2  # 정사각형 넓이 업데이트

print(max_size)
