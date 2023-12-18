import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)