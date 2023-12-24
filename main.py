import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import array
def convert_array_to_bytes(array):
        return array.tobytes()