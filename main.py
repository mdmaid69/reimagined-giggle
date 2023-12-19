import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_power(work, time):
        return work / time