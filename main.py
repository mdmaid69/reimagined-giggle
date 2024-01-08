def count_elements(lst):
        return len(lst)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)