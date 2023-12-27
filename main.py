import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a