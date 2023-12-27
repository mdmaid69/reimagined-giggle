import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)