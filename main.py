import array
def get_array_as_bytearray(array):
        return bytearray(array)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)