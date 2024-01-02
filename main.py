import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)