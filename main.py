import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import array
def get_array_item_count(array, item):
        return array.count(item)