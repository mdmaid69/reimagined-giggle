import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_density(mass, volume):
        return mass / volume