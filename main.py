import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a