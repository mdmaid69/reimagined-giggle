import array
def get_array_buffer_info(array):
        return array.buffer_info()
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)