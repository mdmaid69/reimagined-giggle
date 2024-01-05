import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)