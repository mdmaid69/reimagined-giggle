import re
def split_string(pattern, string):
        return re.split(pattern, string)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a