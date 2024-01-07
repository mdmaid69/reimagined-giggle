import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)