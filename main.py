import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))