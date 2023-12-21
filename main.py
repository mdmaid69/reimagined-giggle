def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))