import re
def split_string(pattern, string):
        return re.split(pattern, string)
import sys
def add_to_python_path(path):
        sys.path.append(path)