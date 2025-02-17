import sys
from collections import deque

# 입력 받기
N, M, V = map(int, sys.stdin.readline().split())  # 정점 개수, 간선 개수, 시작 정점
graph = {i: [] for i in range(1, N + 1)}  # 인접 리스트

# 간선 정보 저장 (양방향 그래프)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 순서대로 탐색하기 위해 정렬
for key in graph:
    graph[key].sort()

# DFS (재귀)
def dfs(v, visited):
    print(v, end=" ")  # 방문한 정점 출력
    visited[v] = True  # 방문 체크
    
    for next_v in graph[v]:  # 현재 정점과 연결된 정점 탐색
        if not visited[next_v]:  # 방문하지 않았다면 재귀 호출
            dfs(next_v, visited)

# BFS (큐)
def bfs(start):
    queue = deque([start])  # 시작 정점을 큐에 삽입
    visited = [False] * (N + 1)  # 방문 체크 배열
    visited[start] = True  # 시작 정점 방문 체크
    
    while queue:
        v = queue.popleft()  # 큐에서 정점 꺼내기
        print(v, end=" ")  # 방문한 정점 출력
        
        for next_v in graph[v]:  # 현재 정점과 연결된 정점 탐색
            if not visited[next_v]:  # 방문하지 않았다면 큐에 추가
                queue.append(next_v)
                visited[next_v] = True

# 방문 배열 초기화 후 실행
visited = [False] * (N + 1)
dfs(V, visited)
print()  # 줄 바꿈
bfs(V)
