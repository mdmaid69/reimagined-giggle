import array
def get_bytes_from_array(array):
        return array.tobytes()
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)