import sys
def print_python_version():
        print(sys.version)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)