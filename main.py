import sys
print(sys.version)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)