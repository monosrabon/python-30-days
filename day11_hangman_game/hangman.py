import random
from words import words_list
from hangman_stages import stages

def choose_word():
    """Select a random word with hint"""
    return random.choice(words_list)

def display_word(word, guessed_letters):
    """Return word with guessed letters revealed"""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game():
    data = choose_word()
    word = data['word']
    hint = data['hint']
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = len(stages) - 1
    hint_used = False

    print("🎮 Welcome to Hangman!")
    print(stages[wrong_guesses])
    print(display_word(word, guessed_letters))

    while wrong_guesses < max_wrong:
        guess = input("Guess a letter (or type 'hint' for a hint): ").lower()

        if guess == "hint":
            if not hint_used:
                print(f"💡 Hint: {hint}")
                hint_used = True
            else:
                print("⚠️ You already used your hint!")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            print("❌ Wrong!")
            wrong_guesses += 1

        print(stages[wrong_guesses])
        print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("🏆 Congratulations! You guessed the word!")
            break
    else:
        print(f"💀 You lost! The word was '{word}'.")
