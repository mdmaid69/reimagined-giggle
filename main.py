import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)