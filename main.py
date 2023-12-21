import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)