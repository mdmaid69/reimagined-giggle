import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))