import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a