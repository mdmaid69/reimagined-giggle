import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)