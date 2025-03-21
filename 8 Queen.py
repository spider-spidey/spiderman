def print_solution(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False
        if col + (row - i) < len(board) and board[i][col + (row - i)] == 1:
            return False
    return True

def solve_n_queens(board, row):
    if row == len(board):
        print_solution(board)
        return True
    found = False
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            found = solve_n_queens(board, row + 1) or found
            board[row][col] = 0
    return found

n = 8
board = [[0] * n for _ in range(n)]
if not solve_n_queens(board, 0):
    print("No solution found")
