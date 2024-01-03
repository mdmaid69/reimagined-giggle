import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
def calculate_energy(mass, c=3*10**8):
        return mass * c**2