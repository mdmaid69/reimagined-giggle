import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))