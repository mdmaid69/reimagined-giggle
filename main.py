import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import array
def get_array_as_bytes(array):
        return bytes(array)