import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)