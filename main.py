import array
def get_array_buffer_info(array):
        return array.buffer_info()
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a