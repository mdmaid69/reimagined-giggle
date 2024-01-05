import array
def get_array_slice(array, i, j):
        return array[i:j]
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a