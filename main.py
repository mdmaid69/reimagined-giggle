import array
def set_array_item(array, i, item):
        array[i] = item
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()