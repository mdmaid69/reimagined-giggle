import array
def get_array_as_complex(array):
        return complex(array[0])
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()