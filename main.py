import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import array
def get_array_as_set(array):
        return set(array)