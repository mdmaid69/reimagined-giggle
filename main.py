import array
def set_array_item(array, i, item):
        array[i] = item
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a