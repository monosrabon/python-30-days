# Helper functions to create, display and inspect the game board.

def create_board():
    """Return a new 3x3 board as a list of 9 spaces."""
    return [" "] * 9

def display_board(board):
    """
    Print the board to the console.
    Board is a list of length 9:
      index: 0 1 2
             3 4 5
             6 7 8
    Display uses 1-9 positions for player convenience.
    """
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}    1 | 2 | 3")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}    4 | 5 | 6")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}    7 | 8 | 9")
    print()

def is_position_free(board, pos):
    """Return True if board position (0-based) is empty."""
    return board[pos] == " "

def is_board_full(board):
    """Return True if no empty spaces left."""
    return all(cell != " " for cell in board)

def check_winner(board):
    """
    Check for a winner.
    Returns "X" or "O" if someone won, otherwise None.
    """
    # All winning index combinations
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None
