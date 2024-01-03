import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)