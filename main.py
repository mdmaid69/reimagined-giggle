import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a