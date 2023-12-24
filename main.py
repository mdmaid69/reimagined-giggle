import array
def convert_array_to_bytes(array):
        return array.tobytes()
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)