import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)