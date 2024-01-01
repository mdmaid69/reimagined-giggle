import array
def get_string_from_array(array):
        return array.tobytes()
import re
def split_string(pattern, string):
        return re.split(pattern, string)