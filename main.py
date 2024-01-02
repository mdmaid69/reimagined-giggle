def calculate_simple_interest(principal, rate, time):
        return principal * rate * time
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)