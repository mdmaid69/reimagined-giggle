import array
def remove_from_array(array, item):
        array.remove(item)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)