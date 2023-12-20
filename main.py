import sys
print(sys.version)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)