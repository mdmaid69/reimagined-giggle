import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)