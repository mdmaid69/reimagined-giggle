import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))