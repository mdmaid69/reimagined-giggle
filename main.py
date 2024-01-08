import array
def extend_array(array, iterable):
        array.extend(iterable)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a