import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2