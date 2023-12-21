import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import array
def get_array_as_complex(array):
        return complex(array[0])