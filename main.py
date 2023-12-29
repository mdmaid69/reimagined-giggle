import array
def get_array_as_frozenset(array):
        return frozenset(array)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)