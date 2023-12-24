import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)