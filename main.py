import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))