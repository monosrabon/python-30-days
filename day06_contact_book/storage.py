import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            try:
                data = f.read().strip()
                if not data:   # if file is empty
                    return {}
                return json.loads(data)
            except json.JSONDecodeError:
                return {}
    return {}

def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)
