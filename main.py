import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import re
def split_string(pattern, string):
        return re.split(pattern, string)