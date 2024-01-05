import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)