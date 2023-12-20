import sys
def add_to_python_path(path):
        sys.path.append(path)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)