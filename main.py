import sys
print(sys.version)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)