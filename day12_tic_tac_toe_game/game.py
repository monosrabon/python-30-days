# Implements the Tic-Tac-Toe game loop and move handling.

from board import create_board, display_board, is_position_free, is_board_full, check_winner

def get_player_move(player, board):
    """
    Prompt the player for a move (1-9).
    Validate input and return 0-based index when valid.
    """
    while True:
        choice = input(f"Player {player} - enter position (1-9): ").strip()
        if not choice.isdigit():
            print("⚠️ Please enter a number from 1 to 9.")
            continue
        pos = int(choice) - 1
        if pos < 0 or pos > 8:
            print("⚠️ Position must be between 1 and 9.")
            continue
        if not is_position_free(board, pos):
            print("⚠️ That position is already taken. Choose another.")
            continue
        return pos

def play_round():
    """
    Play a single game of Tic-Tac-Toe between two local players.
    Returns: "X" or "O" for winner, "Draw" for tie.
    """
    board = create_board()
    current_player = "X"  # X always goes first

    print("\nNew game started! X goes first.")
    display_board(board)

    while True:
        pos = get_player_move(current_player, board)
        board[pos] = current_player

        display_board(board)

        winner = check_winner(board)
        if winner:
            print(f"🏆 Player {winner} wins!")
            return winner

        if is_board_full(board):
            print("🤝 It's a draw!")
            return "Draw"

        # Switch player
        current_player = "O" if current_player == "X" else "X"
