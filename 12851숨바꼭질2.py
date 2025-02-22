from collections import deque

def bfs(N, K):
    queue = deque([(N, 0)])  # (현재 위치, 경과 시간)
    visited = [-1] * 100001  # 방문 시간 저장 (-1은 방문하지 않았음을 의미)
    count = [0] * 100001  # 해당 시간으로 도달하는 방법의 수

    visited[N] = 0  # 시작점 방문 처리
    count[N] = 1  # 시작점에서 시작하는 경우의 수는 1

    while queue:
        x, time = queue.popleft()  # 현재 위치, 경과 시간

        for next_x in (x - 1, x + 1, 2 * x):  # 3가지 이동 방식
            if 0 <= next_x <= 100000:
                # 아직 방문하지 않은 경우 (최초 방문)
                if visited[next_x] == -1:
                    visited[next_x] = time + 1
                    count[next_x] = count[x]  # 현재 위치까지 온 방법의 수 그대로 전달
                    queue.append((next_x, time + 1))
                
                # 방문한 적이 있지만, 현재 최단 시간과 동일한 경우 -> 방법 추가
                elif visited[next_x] == time + 1:
                    count[next_x] += count[x]

    return visited[K], count[K]  # 최단 시간과 방법 수 반환

# 입력 받기
N, K = map(int, input().split())
min_time, num_ways = bfs(N, K)

# 출력
print(min_time)
print(num_ways)
