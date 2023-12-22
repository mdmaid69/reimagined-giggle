import array
def get_bytes_from_array(array):
        return array.tobytes()
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)