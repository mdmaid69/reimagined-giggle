import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a