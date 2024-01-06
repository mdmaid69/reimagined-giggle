import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))