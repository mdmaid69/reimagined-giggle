import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)