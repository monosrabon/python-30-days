# storage.py
import json
from expense import Expense

FILE = "expenses.json"

def load_expenses():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            return [Expense.from_dict(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump([exp.to_dict() for exp in expenses], f, indent=4)
