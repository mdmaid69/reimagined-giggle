import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()