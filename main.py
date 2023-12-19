import array
def get_array_slice(array, i, j):
        return array[i:j]
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)