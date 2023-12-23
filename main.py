import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)