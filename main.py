import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}