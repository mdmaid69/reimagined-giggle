import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
from collections import Counter
print(Counter("hello world"))