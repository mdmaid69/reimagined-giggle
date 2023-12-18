import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import array
def convert_array_to_unicode(array):
        return array.tounicode()