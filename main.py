import array
def get_array_as_memoryview(array):
        return memoryview(array)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)