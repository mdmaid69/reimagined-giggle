import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import array
def get_array_as_frozenset(array):
        return frozenset(array)