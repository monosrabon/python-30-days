
def get_grade(score, total):
    if score == total:
        return "A (Excellent 🎉)"
    elif score == total - 1:
        return "B (Good 🙂)"
    elif score == 1:
        return "C (Needs Improvement 🤔)"
    else:
        return "F (Better luck next time 😢)"
