import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)