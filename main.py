import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)