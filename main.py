import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)