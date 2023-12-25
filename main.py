import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_energy(mass, c=3*10**8):
        return mass * c**2