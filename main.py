import array
def get_array_as_set(array):
        return set(array)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)