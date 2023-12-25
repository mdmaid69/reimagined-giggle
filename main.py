import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)