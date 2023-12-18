import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)