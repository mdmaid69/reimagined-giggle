import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import array
def set_array_item(array, i, item):
        array[i] = item