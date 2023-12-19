import array
def get_string_from_array(array):
        return array.tobytes()
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)