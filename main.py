import array
def get_bytes_from_array(array):
        return array.tobytes()
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)