import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)