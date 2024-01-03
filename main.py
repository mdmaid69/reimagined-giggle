import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)