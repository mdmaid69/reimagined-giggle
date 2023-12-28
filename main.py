import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)