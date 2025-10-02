
import random
from questions import quiz_questions
from grader import get_grade

def start_quiz():
    print("\n🎯 Welcome to the Quiz Game!")
    print("You will get 3 random questions. Let's test your knowledge!\n")

    # Pick 3 random unique questions
    selected_questions = random.sample(quiz_questions, 3)

    score = 0  # Track correct answers

    for i, q in enumerate(selected_questions, 1):
        print(f"Q{i}: {q['question']}")
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == q['answer'].lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is: {q['answer']}\n")

    # Show result
    print("🎓 Quiz Finished!")
    print(f"Your Score: {score}/3")
    print(f"Your Grade: {get_grade(score, 3)}\n")
