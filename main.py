import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a