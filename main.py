import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def square_number(x):
        return x**2