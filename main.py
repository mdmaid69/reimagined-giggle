import math
def calculate_sign(x):
        return math.copysign(1, x)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)