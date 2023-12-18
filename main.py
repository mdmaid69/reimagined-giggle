import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)