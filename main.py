import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_energy(mass, c=3*10**8):
        return mass * c**2