import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))