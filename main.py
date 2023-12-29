import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)