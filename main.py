import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import re
def split_string(pattern, string):
        return re.split(pattern, string)