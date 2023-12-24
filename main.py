import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
from collections import Counter
print(Counter("hello world"))