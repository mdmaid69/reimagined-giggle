import array
def get_array_as_bytearray(array):
        return bytearray(array)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a