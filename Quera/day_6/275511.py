n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

max_eliminated = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'W':
            dp = [[-1 for _ in range(m)] for _ in range(n)]
            dp[i][j] = 0
            for x in range(i, 0, -1):
                for y in range(m):
                    if dp[x][y] != -1:
                        for dy in [-1, 0, 1]:
                            nx, ny = x - 1, y + dy
                            if 0 <= nx < n and 0 <= ny < m:
                                if board[nx][ny] != 'W':
                                    gain = 1 if board[nx][ny] == 'B' else 0
                                    dp[nx][ny] = max(dp[nx][ny], dp[x][y] + gain)
            current_max = max([max(row) for row in dp])
            max_eliminated = max(max_eliminated, current_max)

print(max_eliminated)
