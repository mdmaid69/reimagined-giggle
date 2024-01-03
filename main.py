import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)