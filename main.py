import array
def get_array_typecode(array):
        return array.typecode
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)