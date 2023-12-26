import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a