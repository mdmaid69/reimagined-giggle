import re
def split_string(pattern, string):
        return re.split(pattern, string)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)