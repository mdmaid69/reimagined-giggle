import array
def get_array_as_bytearray(array):
        return bytearray(array)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()