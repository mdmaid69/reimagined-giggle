import sys
print(sys.version)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)