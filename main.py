import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height