def calculate_force(mass, acceleration):
        return mass * acceleration
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)