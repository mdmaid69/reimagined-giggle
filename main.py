import array
def get_array_as_frozenset(array):
        return frozenset(array)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)