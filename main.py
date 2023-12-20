import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)