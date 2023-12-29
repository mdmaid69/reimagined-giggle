import sys
def add_to_python_path(path):
        sys.path.append(path)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)