import array
def get_array_buffer_info(array):
        return array.buffer_info()
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)