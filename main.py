def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)