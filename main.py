import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import sys
def print_python_version():
        print(sys.version)