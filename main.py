def find_min(numbers):
        return min(numbers)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)