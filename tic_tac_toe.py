import math

HUMAN = "X"
AI = "O"
EMPTY = " "

def create_board():
    return [EMPTY] * 9

def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])
    print("\n")

def is_empty(board, pos):
    return board[pos] == EMPTY

def available_moves(board):
    return [i for i in range(9) if board[i] == EMPTY]

def check_winner(board, player):
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),     # rows
        (0,3,6),(1,4,7),(2,5,8),     # columns
        (0,4,8),(2,4,6)              # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_positions)

def is_terminal(board):
    return check_winner(board, HUMAN) or check_winner(board, AI) or len(available_moves(board)) == 0

def minimax(board, depth, alpha, beta, maximizing):
    if check_winner(board, AI):
        return 10 - depth
    if check_winner(board, HUMAN):
        return depth - 10
    if len(available_moves(board)) == 0:
        return 0

    if maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, alpha, beta, False)
            board[move] = EMPTY
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score

    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = HUMAN
            score = minimax(board, depth + 1, alpha, beta, True)
            board[move] = EMPTY
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score

def ai_move(board):
    best_score = -math.inf
    move = None
    for m in available_moves(board):
        board[m] = AI
        score = minimax(board, 0, -math.inf, math.inf, False)
        board[m] = EMPTY
        if score > best_score:
            best_score = score
            move = m
    
    board[move] = AI

def play_game():
    board = create_board()
    print("Human = X | AI = O")
    
    while not is_terminal(board):
        print_board(board)
        
        # Human move
        try:
            move = int(input("Enter your move (0-8): "))
            if move not in available_moves(board):
                print("Invalid move. Try again.")
                continue
            board[move] = HUMAN
        except:
            print("Invalid input.")
            continue
        
        if is_terminal(board):
            break
        
        # AI move
        ai_move(board)

    print_board(board)
    
    if check_winner(board, HUMAN):
        print("You Win!")
    elif check_winner(board, AI):
        print("AI Wins!")
    else:
        print("It's a Draw!")


if __name__ == "__main__":
    play_game()
