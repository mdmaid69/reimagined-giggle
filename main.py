import sys
def add_to_python_path(path):
        sys.path.append(path)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)