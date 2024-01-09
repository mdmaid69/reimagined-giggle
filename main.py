import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)