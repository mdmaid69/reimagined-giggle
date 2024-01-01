import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))