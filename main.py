import array
def extend_array(array, iterable):
        array.extend(iterable)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()