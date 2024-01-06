import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)