def find_min(lst):
        return min(lst)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)