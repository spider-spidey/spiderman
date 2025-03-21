import math

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])

def check_winner(board, player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8),
                       (0,3,6), (1,4,7), (2,5,8),
                       (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def alpha_beta(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, 'X'):
        return -10 + depth
    elif check_winner(board, 'O'):
        return 10 - depth
    elif ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = alpha_beta(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = alpha_beta(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = alpha_beta(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    board = [' ' for _ in range(9)]
    print_board(board)
    while True:
        player_move = int(input("Enter your move (0-8): "))
        if board[player_move] == ' ':
            board[player_move] = 'X'
        else:
            print("Invalid move. Try again.")
            continue
        if check_winner(board, 'X'):
            print_board(board)
            print("You Win!")
            break
        elif ' ' not in board:
            print_board(board)
            print("It's a Draw!")
            break

        print("AI is thinking...")
        ai_move = best_move(board)
        board[ai_move] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("AI Wins!")
            break
        elif ' ' not in board:
            print("It's a Draw!")
            break

play_game()
