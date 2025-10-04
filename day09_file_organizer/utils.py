# Helper functions (check & create folders)
import os

def create_folder_if_not_exists(path):
    """Create a folder if it doesn’t already exist."""
    if not os.path.exists(path):
        os.makedirs(path)
