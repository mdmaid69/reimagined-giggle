import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import array
def get_array_as_set(array):
        return set(array)