import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)