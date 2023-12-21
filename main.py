def calculate_area(radius):
        return 3.14 * radius * radius
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)