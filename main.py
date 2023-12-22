import array
def get_array_as_list(array):
        return list(array)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)