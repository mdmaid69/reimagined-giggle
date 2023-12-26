import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import array
def get_bytes_from_array(array):
        return array.tobytes()