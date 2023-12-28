import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import array
def extend_array(array, iterable):
        array.extend(iterable)