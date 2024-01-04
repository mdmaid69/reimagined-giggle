def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)