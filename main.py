import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def cube_number(x):
        return x**3