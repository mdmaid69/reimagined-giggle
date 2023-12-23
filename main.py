import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def find_min(lst):
        return min(lst)