import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import array
def convert_array_to_list(array):
        return array.tolist()