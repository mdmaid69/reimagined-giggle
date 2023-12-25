import array
def check_if_array_contains_item(array, item):
        return item in array
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)