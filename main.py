import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a