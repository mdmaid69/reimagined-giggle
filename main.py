import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)