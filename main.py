import os
print(os.getcwd())
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)