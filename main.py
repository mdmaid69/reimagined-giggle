import random
def roll_die():
        return random.randint(1, 6)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2