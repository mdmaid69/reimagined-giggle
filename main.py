import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)