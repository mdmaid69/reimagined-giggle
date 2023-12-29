import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_pressure(force, area):
        return force / area