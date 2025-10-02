# main.py

from quiz import start_quiz

if __name__ == "__main__":
    while True:
        start_quiz()
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Thanks for playing! Goodbye!")
            break
