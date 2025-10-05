import json
import random

FLASHCARD_FILE = "flashcards.json"

def load_flashcards():
    """Load flashcards from JSON file"""
    try:
        with open(FLASHCARD_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_flashcards(flashcards):
    """Save flashcards to JSON file"""
    with open(FLASHCARD_FILE, "w") as f:
        json.dump(flashcards, f, indent=4)

def add_flashcard(question, answer):
    """Add a new flashcard"""
    flashcards = load_flashcards()
    flashcards.append({"question": question, "answer": answer})
    save_flashcards(flashcards)

def get_random_flashcards(count=5):
    """Get a random set of flashcards"""
    flashcards = load_flashcards()
    return random.sample(flashcards, min(count, len(flashcards)))
