import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)