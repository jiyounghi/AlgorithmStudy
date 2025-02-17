""""
1. 아이디어 
- 2중 for => 값 1 && 방문 X => BFS
- BFS 돌면서 그림 개수 +1, 최대값 갱신 

2. 시간복잡도
- BFS : O(V+E)
- V : 500 * 500 
- E : 4 * 500 * 500
- V*E : 5 * 250000 = 100만 < 2억 >> 가능! 

3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)
"""

import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    rs = 1 
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        # 동서남북 네 방향으로 옮겨주면서 새로운 1이 있는지 확인
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m: # 사이즈가 넘어가지 않는지 확인
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    rs += 1 # 새로운 1 발견할 때마다 증가 
                    chk[ny][nx] = True 
                    q.append(ny.nx)
    return rs # 전체 크기 

cnt = 0 
maxv = 0 
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            # 전체 그림 갯수를 +1 
            cnt += 1
            # BFS > 그림 크기를 구해주고 
            maxv = max(maxv, bfs(j,i))
            # 최대값 갱신 

print(cnt) # 전체 그림 개수 
print(maxv)