import array
def extend_array(array, iterable):
        array.extend(iterable)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)