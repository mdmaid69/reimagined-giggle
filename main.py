import math
def calculate_error_function(x):
        return math.erf(x)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)