import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a