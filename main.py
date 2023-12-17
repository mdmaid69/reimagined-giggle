import array
def get_array_as_bytes(array):
        return bytes(array)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)