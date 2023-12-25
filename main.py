import array
def convert_array_to_bytes(array):
        return array.tobytes()
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()