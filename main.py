import itertools
print(list(itertools.permutations([1, 2, 3])))
import random
def generate_random_sample(population, k):
        return random.sample(population, k)