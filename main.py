import array
def get_array_as_memoryview(array):
        return memoryview(array)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()