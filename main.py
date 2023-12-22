import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)