import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a