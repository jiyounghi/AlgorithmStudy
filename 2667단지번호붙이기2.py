n = int(input()) 
m = [list(map(int,input().strip())) for _ in range(n)]

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    m[x][y] = 0
    stack = []
    stack.append([x,y])
    cnt = 1
    
    while stack:
        sx, sy = stack.pop()
        for i in range(4):
            nx, ny = sx+dx[i], sy+dy[i]
            if 0<=nx<n and 0<=ny<n and m[nx][ny] == 1:
                m[nx][ny] = 0
                stack.append([nx,ny])
                cnt += 1
    return cnt 

lst = []
for x in range(n):
    for y in range(n):
        if m[x][y] == 1:
            cnt = dfs(x, y)  
            lst.append(cnt)

print(len(lst))            
lst.sort()
for i in lst:
    print(i)
            