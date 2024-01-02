import array
def get_array_itemsize(array):
        return array.itemsize
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)