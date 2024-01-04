import os
def list_files_in_directory(path):
        return os.listdir(path)
import sys
def add_to_python_path(path):
        sys.path.append(path)