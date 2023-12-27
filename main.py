import collections
def create_counter():
        return collections.Counter()
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)