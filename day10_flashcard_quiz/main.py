from flashcards import add_flashcard, get_random_flashcards
from quiz import run_quiz

def main():
    while True:
        print("\n==== Flashcard Quiz App ====")
        print("1. Add a flashcard")
        print("2. Start quiz")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            question = input("Enter question: ")
            answer = input("Enter answer: ")
            add_flashcard(question, answer)
            print("✅ Flashcard added successfully!")

        elif choice == "2":
            flashcards = get_random_flashcards(5)
            if flashcards:
                run_quiz(flashcards)
            else:
                print("⚠️ No flashcards available. Please add some first.")

        elif choice == "3":
            print("👋 Goodbye! See you next time.")
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()
