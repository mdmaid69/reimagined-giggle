import re
def split_string(pattern, string):
        return re.split(pattern, string)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a