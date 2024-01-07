import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)