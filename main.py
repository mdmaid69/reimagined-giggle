import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def calculate_roi(gain, cost):
        return (gain - cost) / cost