import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import array
def check_if_array_contains_item(array, item):
        return item in array