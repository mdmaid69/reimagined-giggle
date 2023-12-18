import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import array
def check_if_array_contains_item(array, item):
        return item in array