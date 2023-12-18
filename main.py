import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)