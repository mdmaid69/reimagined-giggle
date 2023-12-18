import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import array
def get_array_slice(array, i, j):
        return array[i:j]