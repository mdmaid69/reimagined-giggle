import array
def get_array_item(array, i):
        return array[i]
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)