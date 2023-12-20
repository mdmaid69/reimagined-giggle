import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)