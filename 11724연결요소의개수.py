import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 설정
input = sys.stdin.readline

def dfs(node):
    visited[node] = True  # 현재 노드 방문 처리
    for neighbor in graph[node]:  # 인접한 노드들 탐색
        if not visited[neighbor]:  
            dfs(neighbor)

# 입력 받기
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

# 간선 정보 입력
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프

# 연결 요소 개수 탐색
count = 0
for i in range(1, N + 1):
    if not visited[i]:  # 방문하지 않은 노드 발견
        dfs(i)  # DFS 수행
        count += 1  # 연결 요소 개수 증가

print(count)  # 결과 출력
