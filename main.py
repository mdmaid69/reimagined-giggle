import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)