import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable