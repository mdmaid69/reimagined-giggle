import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import array
def get_array_as_str(array):
        return str(array)