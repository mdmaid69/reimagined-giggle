def calculate_roi(gain, cost):
        return (gain - cost) / cost
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)