import re
def split_string(pattern, string):
        return re.split(pattern, string)
import array
def get_array_as_frozenset(array):
        return frozenset(array)