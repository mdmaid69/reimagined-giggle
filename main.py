import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)