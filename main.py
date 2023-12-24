import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"