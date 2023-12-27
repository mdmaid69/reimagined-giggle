import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)