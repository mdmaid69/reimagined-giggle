import array
def clear_array(array):
        array *= 0
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)