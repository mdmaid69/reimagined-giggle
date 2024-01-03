import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)