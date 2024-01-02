import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height