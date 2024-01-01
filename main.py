import array
def get_array_as_bytes(array):
        return bytes(array)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)