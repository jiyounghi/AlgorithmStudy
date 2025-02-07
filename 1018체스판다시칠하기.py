def count_repaints(board, start_row, start_col):
    w_start, b_start = 0, 0  # 왼쪽 위가 'W'일 때와 'B'일 때 다시 칠해야 하는 개수

    for i in range(8):
        for j in range(8):
            # 현재 위치에서 원래 체스판 색상을 계산
            if (i + j) % 2 == 0:  # (짝수) 왼쪽 위와 같은 색이어야 함
                if board[start_row + i][start_col + j] != 'W':
                    w_start += 1  # 'W'로 칠해야 하는 경우
                if board[start_row + i][start_col + j] != 'B':
                    b_start += 1  # 'B'로 칠해야 하는 경우
            else:  # (홀수) 왼쪽 위와 반대 색이어야 함
                if board[start_row + i][start_col + j] != 'B':
                    w_start += 1  # 'B'로 칠해야 하는 경우
                if board[start_row + i][start_col + j] != 'W':
                    b_start += 1  # 'W'로 칠해야 하는 경우

    return min(w_start, b_start)  # 두 패턴 중 최소값 반환


n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]  # 입력 받기

min_repaints = float('inf')

# 8×8 체스판을 만들 수 있는 모든 위치에서 검사
for i in range(n - 7):
    for j in range(m - 7):
        min_repaints = min(min_repaints, count_repaints(board, i, j))

print(min_repaints)
