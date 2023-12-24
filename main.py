import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))