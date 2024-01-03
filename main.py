import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)