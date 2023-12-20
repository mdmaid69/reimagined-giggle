import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import array
def extend_array(array, iterable):
        array.extend(iterable)