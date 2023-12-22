import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a