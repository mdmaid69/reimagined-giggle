import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)