import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import sys
def print_python_version():
        return sys.version