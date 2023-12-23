import array
def clear_array(array):
        array *= 0
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)