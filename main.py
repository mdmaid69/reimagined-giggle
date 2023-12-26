import array
def get_string_from_array(array):
        return array.tobytes()
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)