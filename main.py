import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a