import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))