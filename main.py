import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import array
def insert_into_array(array, i, item):
        array.insert(i, item)