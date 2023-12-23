import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)