import re
def split_string(pattern, string):
        return re.split(pattern, string)
from collections import Counter
print(Counter("hello world"))