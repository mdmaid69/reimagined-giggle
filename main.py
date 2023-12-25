import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def add_numbers(x, y):
        return x + y