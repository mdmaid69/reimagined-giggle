import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)