import array
def get_array_item_count(array, item):
        return array.count(item)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)