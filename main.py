import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)