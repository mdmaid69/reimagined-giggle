import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array