import array
def get_bytes_from_array(array):
        return array.tobytes()
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)