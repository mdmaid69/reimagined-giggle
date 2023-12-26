import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)