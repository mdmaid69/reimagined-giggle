import os
print(os.getcwd())
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)