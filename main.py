import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)