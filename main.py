import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)