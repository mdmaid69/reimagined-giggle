import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_area_rectangle(l, w):
        return l * w