import array
def get_array_as_bytes(array):
        return bytes(array)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)