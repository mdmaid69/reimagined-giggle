import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import array
def get_array_as_frozenset(array):
        return frozenset(array)