import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)