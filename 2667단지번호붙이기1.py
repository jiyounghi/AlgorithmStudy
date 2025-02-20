import sys

# 입력 받기
n = int(input().strip())
map_data = [list(map(int, input().strip())) for _ in range(n)]

# 이동 방향 (동, 서, 남, 북)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    stack = [(x, y)]
    map_data[x][y] = 0  # 방문 처리
    count = 1  # 현재 단지의 집 개수

    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and map_data[nx][ny] == 1:
                map_data[nx][ny] = 0  # 방문 처리
                stack.append((nx, ny))
                count += 1
    
    return count

# 단지 개수 저장 리스트
danji = []

# 지도 순회하며 단지 찾기
for i in range(n):
    for j in range(n):
        if map_data[i][j] == 1:
            danji.append(dfs(i, j))

# 결과 출력
danji.sort()
print(len(danji))
for d in danji:
    print(d)
