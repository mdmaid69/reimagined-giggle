import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import array
def get_array_buffer_info(array):
        return array.buffer_info()