import sys
def exit_program():
        sys.exit()
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)