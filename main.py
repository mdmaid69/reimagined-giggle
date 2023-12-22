import array
def get_string_from_array(array):
        return array.tobytes()
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)