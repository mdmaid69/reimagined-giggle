import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_roi(gain, cost):
        return (gain - cost) / cost