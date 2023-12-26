import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array