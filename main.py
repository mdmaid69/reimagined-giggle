import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3