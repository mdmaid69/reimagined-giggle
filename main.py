import array
def append_to_array(array, item):
        array.append(item)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)