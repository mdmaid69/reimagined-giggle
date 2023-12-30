import math
def calculate_sign(x):
        return math.copysign(1, x)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable