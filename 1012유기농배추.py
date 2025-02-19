import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 증가 (DFS 대비)

def dfs(x, y, farm, visited, M, N):
    # 상, 하, 좌, 우 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited[y][x] = True  # 방문 처리

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 범위 내에 있고, 방문하지 않았으며 배추가 있는 경우 DFS 탐색
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and farm[ny][nx] == 1:
            dfs(nx, ny, farm, visited, M, N)

def solve():
    T = int(input().strip())  # 테스트 케이스 개수

    results = []
    
    for _ in range(T):
        # M: 가로 크기, N: 세로 크기, K: 배추 개수
        M, N, K = map(int, input().strip().split())

        # 배추밭과 방문 배열 초기화
        farm = [[0] * M for _ in range(N)]
        visited = [[False] * M for _ in range(N)]

        # 배추 위치 입력받기
        for _ in range(K):
            X, Y = map(int, input().strip().split())
            farm[Y][X] = 1  # 배추 심기 (주의: Y가 행, X가 열)

        worm_count = 0  # 필요한 배추흰지렁이 개수

        # 모든 좌표를 돌면서 DFS 실행
        for y in range(N):
            for x in range(M):
                if farm[y][x] == 1 and not visited[y][x]:  # 배추가 있고 방문하지 않았으면
                    dfs(x, y, farm, visited, M, N)
                    worm_count += 1  # 새로운 지렁이 필요

        results.append(str(worm_count))  # 결과 저장

    print("\n".join(results))  # 최종 출력

if __name__ == "__main__":
    solve()
