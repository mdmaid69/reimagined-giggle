import array
def remove_from_array(array, item):
        array.remove(item)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a