import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def calculate_energy(mass, c=3*10**8):
        return mass * c**2