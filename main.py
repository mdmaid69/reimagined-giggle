import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import re
def split_string(pattern, string):
        return re.split(pattern, string)