import sys
def exit_program():
        sys.exit()
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)