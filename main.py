import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)