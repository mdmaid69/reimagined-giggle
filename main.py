import os
print(os.getcwd())
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)