def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)