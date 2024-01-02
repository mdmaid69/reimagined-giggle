import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a