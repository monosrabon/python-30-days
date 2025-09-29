import string

def check_strength(password):
    length = len(password)
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_symbol = any(ch in string.punctuation for ch in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length < 6 or score < 2:
        return "❌ Weak Password"
    elif length >= 6 and score >= 2:
        return "⚠️ Medium Password"
    elif length >= 10 and score == 4:
        return "✅ Strong Password"
    else:
        return "⚠️ Medium Password"
