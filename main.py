import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)