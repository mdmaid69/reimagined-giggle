import array
def get_array_as_complex(array):
        return complex(array[0])
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)