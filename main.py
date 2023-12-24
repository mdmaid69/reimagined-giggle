import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2