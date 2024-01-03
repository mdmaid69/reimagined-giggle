import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)