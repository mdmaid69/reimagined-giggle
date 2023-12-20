import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable