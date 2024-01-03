import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)