import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import re
def split_string(pattern, string):
        return re.split(pattern, string)