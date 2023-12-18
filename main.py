def calculate_roi(gain, cost):
        return (gain - cost) / cost
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)