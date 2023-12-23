import array
def get_bytes_from_array(array):
        return array.tobytes()
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a