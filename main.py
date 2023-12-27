import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import sys
def add_to_python_path(path):
        sys.path.append(path)