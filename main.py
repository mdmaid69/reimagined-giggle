def find_max(numbers):
        return max(numbers)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)