import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a