import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)