import array
def append_to_array(array, item):
        array.append(item)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)