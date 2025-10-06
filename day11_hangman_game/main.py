from hangman import play_game

def main():
    while True:
        print("\n==== Hangman Game ====")
        print("1. Play Hangman")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()
