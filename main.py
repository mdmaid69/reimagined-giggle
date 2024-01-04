import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)