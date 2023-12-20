import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))