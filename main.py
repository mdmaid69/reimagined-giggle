import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)