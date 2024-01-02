import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)