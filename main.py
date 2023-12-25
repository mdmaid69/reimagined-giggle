import math
def calculate_sign(x):
        return math.copysign(1, x)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)