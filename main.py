import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_roi(gain, cost):
        return (gain - cost) / cost