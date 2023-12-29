import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import sys
def print_python_version():
        return sys.version