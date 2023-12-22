import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height