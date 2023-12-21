import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)