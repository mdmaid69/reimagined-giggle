import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a