import array
def convert_array_to_list(array):
        return array.tolist()
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a