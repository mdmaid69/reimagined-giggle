import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import array
def get_array_slice(array, i, j):
        return array[i:j]