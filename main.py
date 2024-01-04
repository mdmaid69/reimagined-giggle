import array
def set_array_item(array, i, item):
        array[i] = item
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)