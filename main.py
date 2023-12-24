import random
def generate_random_sample(population, k):
        return random.sample(population, k)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2