import sys
def exit_program():
        sys.exit()
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)