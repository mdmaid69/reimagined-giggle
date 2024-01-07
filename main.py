import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)