import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import array
def get_array_item(array, i):
        return array[i]