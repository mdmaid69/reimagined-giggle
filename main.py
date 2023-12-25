import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
from collections import Counter
print(Counter("hello world"))