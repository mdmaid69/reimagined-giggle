import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))