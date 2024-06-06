import os
import sys

def add_to_path(folder_path) -> None:
    """
    Function takes
    folder_path: str
    as an input and adds it to path if it is not already
    """
    current_path = os.environ.get('PATH', '')
    if folder_path not in current_path:
        os.environ['PATH'] += os.pathsep + folder_path
        print(f"Added {folder_path} to PATH")
    else:
        print(f"{folder_path} is already in PATH")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder_to_add = sys.argv[1]
        add_to_path(folder_to_add)
    else:
        print("No folder path provided.")
