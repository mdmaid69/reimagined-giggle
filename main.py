import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()