import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)