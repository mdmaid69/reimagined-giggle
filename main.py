import array
def get_array_as_bytes(array):
        return bytes(array)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)