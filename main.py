import sys
def print_python_version():
        print(sys.version)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)