import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))