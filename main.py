import array
def get_array_index(array, item):
        return array.index(item)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)