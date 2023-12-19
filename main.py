import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)