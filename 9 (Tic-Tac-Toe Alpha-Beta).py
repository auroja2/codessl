import random

# Constants for the board
EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'

# Check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Check if the game is a draw
def is_draw(board):
    return all(board[i][j] != EMPTY for i in range(3) for j in range(3))

# Check if the board is full
def is_board_full(board):
    return all(board[i][j] != EMPTY for i in range(3) for j in range(3))

# Evaluate the board
def evaluate(board):
    if check_winner(board, PLAYER_X):
        return 10  # AI wins
    elif check_winner(board, PLAYER_O):
        return -10  # User wins
    else:
        return 0  # Draw or ongoing game

# Alpha-Beta Pruning function
def alpha_beta(board, depth, alpha, beta, maximizing_player):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = alpha_beta(board, depth + 1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = alpha_beta(board, depth + 1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# AI makes the best move using Alpha-Beta Pruning
def best_move(board):
    best_val = -float('inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_val = alpha_beta(board, 0, -float('inf'), float('inf'), False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Display the board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Player makes their move
def player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row col): ").split())
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_O
                break
            else:
                print("The cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column values between 0 and 2.")

# Main game function
def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are Player O (X is the AI).")
    
    # Main game loop
    while True:
        print_board(board)
        
        # Player's turn
        player_move(board)
        if check_winner(board, PLAYER_O):
            print_board(board)
            print("You win!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI's turn (Alpha-Beta Pruning)
        print("AI's turn...")
        row, col = best_move(board)
        board[row][col] = PLAYER_X
        if check_winner(board, PLAYER_X):
            print_board(board)
            print("AI wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

# Main function to start the game
if __name__ == "__main__":
    play_game()
