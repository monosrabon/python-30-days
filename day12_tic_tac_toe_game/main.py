# Entry point: runs rounds and asks to play again. Basic per-session scoreboard.

from game import play_round

def main():
    print("=== Tic-Tac-Toe (Day 12) ===")
    scores = {"X": 0, "O": 0, "Draw": 0}

    while True:
        result = play_round()
        scores[result] = scores.get(result, 0) + 1

        print("\nSession scores:")
        print(f"  X wins: {scores.get('X',0)}")
        print(f"  O wins: {scores.get('O',0)}")
        print(f"  Draws : {scores.get('Draw',0)}")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
