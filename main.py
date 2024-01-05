import collections
def count_elements(iterable):
        return collections.Counter(iterable)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2