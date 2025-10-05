def run_quiz(flashcards):
    """Run the quiz with given flashcards"""
    print("\n🎴 Starting Quiz 🎴\n")
    score = 0

    for i, card in enumerate(flashcards, start=1):
        print(f"Q{i}: {card['question']}")
        answer = input("Your answer: ")

        if answer.strip().lower() == card['answer'].strip().lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct Answer: {card['answer']}\n")

    print(f"Quiz Completed! 🎉 Your Score: {score}/{len(flashcards)}")
    if score == len(flashcards):
        print("🏆 Excellent! All correct!")
    elif score >= len(flashcards)//2:
        print("👍 Good job! Keep practicing.")
    else:
        print("📚 You need more practice.")
