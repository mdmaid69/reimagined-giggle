import array
def get_array_itemsize(array):
        return array.itemsize
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a