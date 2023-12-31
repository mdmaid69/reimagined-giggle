import collections
def create_stack():
        return collections.deque()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2