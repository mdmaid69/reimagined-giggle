import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}