import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_work(force, distance):
        return force * distance