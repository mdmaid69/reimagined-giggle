import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def calculate_roi(gain, cost):
        return (gain - cost) / cost