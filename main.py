import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import re
def split_string(pattern, string):
        return re.split(pattern, string)