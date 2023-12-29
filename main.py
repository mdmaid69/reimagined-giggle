import random
def generate_random_sample(population, k):
        return random.sample(population, k)
n = 10
print("Powers of 2:", [2**x for x in range(n)])