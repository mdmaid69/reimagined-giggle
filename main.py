import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)