import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)