import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)