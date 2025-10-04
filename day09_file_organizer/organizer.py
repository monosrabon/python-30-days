# Core logic (organizing files)
import os
import shutil
from categories import CATEGORIES
from utils import create_folder_if_not_exists

def organize_files(folder_path):
    """Organize files in the given folder based on their extension."""
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        # Match file extension with categories
        for category, extensions in CATEGORIES.items():
            if file_ext in extensions:
                category_folder = os.path.join(folder_path, category)
                create_folder_if_not_exists(category_folder)
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"✅ Moved: {filename} → {category}/")
                moved = True
                break

        # If no category matches → move to "Others"
        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            create_folder_if_not_exists(other_folder)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"📂 Moved: {filename} → Others/")
