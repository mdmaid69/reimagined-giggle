import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import array
def get_array_as_float(array):
        return float(array[0])