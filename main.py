import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable