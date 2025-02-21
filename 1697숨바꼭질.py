from collections import deque

def bfs(N, K):
    queue = deque([(N, 0)])  # (현재 위치, 경과 시간)
    visited = set()  # 방문한 위치 저장 (중복 탐색 방지)
    visited.add(N)

    while queue:
        x, time = queue.popleft()  # 현재 위치, 경과 시간

        if x == K:  # 동생 위치에 도착하면 종료
            return time

        for next_x in (x - 1, x + 1, 2 * x):  # 3가지 이동 방식
            if 0 <= next_x <= 100000 and next_x not in visited:
                visited.add(next_x)  # 방문 처리
                queue.append((next_x, time + 1))  # 큐에 추가 (새로운 경과 시간)

N, K = map(int, input().split())
print(bfs(N, K))
