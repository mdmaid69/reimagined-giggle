import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a