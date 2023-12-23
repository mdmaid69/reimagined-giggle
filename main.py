import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import sys
def add_to_python_path(path):
        sys.path.append(path)