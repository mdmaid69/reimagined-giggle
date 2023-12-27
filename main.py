import sys
def add_to_python_path(path):
        sys.path.append(path)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)