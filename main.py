import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)