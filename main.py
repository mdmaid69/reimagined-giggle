import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import sys
def add_to_python_path(path):
        sys.path.append(path)