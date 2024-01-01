import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)