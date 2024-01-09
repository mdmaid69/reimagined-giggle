import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import sys
def print_python_version():
        print(sys.version)