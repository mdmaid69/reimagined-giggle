import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))