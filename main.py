import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)