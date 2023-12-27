def calculate_work(force, distance):
        return force * distance
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)