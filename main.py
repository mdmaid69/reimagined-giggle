import os
def get_file_size(filename):
        return os.path.getsize(filename)
import sys
def add_to_python_path(path):
        sys.path.append(path)