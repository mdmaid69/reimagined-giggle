import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a