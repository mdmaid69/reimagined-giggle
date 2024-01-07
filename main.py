import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a