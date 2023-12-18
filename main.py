import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)