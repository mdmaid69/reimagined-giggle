import re
def split_string(pattern, string):
        return re.split(pattern, string)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)