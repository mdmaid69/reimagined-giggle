import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)