import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))