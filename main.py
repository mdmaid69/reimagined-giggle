import array
def get_array_as_int(array):
        return int(array[0])
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a