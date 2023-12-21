def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)