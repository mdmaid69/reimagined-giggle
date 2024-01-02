import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time