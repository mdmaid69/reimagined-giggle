import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)