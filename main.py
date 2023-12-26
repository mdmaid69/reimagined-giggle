import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}