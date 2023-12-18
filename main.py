import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a