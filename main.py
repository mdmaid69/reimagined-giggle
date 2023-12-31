import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)