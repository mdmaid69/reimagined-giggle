import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)