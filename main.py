import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)