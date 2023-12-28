import re
def split_string(pattern, string):
        return re.split(pattern, string)
import array
def get_array_as_memoryview(array):
        return memoryview(array)