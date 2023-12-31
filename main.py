import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))