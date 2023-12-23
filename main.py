import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import itertools
print(list(itertools.permutations([1, 2, 3])))