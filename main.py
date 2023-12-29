import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)