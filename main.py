import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))