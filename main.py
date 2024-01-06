import re
def split_string(pattern, string):
        return re.split(pattern, string)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)