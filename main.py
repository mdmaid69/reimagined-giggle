def calculate_speed(distance, time):
        return distance / time
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)