import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import sys
def print_python_version():
        print(sys.version)