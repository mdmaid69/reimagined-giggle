def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)