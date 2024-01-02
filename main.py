import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import array
def get_array_itemsize(array):
        return array.itemsize