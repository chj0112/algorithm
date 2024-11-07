def check(x, y, n):
    for i in range(9):
        if board[x][i] == n or board[i][y] == n:
            return False
    for i in range((x // 3) * 3, (x // 3) * 3 + 3):
        for j in range((y // 3) * 3, (y // 3) * 3 + 3):
            if board[i][j] == n:
                return False
    return True

def sudoku(k):
    if k == len(zero):
        for i in board:
            print(*i)
        exit()
    for i in range(1, 10):
        x = zero[k][0]
        y = zero[k][1]
        if check(x, y, i):
            board[x][y] = i
            sudoku(k + 1)
            board[x][y] = 0


board = [list(map(int, input().split())) for _ in range(9)]
zero = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero.append([i, j])
sudoku(0)