import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a