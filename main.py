import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable