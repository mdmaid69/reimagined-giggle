import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a