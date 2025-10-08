# Entry point for the Dice Rolling Simulator

from dice import roll_dice
from utils import format_results

def main():
    print("🎲 Welcome to the Dice Rolling Simulator! 🎲")

    while True:
        try:
            sides = int(input("\nEnter number of sides on the dice (default 6): ") or 6)
            count = int(input("Enter how many dice to roll (default 1): ") or 1)

            results = roll_dice(sides, count)
            print(format_results(results))

        except ValueError:
            print("⚠️ Please enter valid numbers.")
            continue

        again = input("\nRoll again? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThanks for playing! Goodbye 👋")
            break

if __name__ == "__main__":
    main()
