import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable