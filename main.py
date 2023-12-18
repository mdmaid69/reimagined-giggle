import random
def generate_random_sample(population, k):
        return random.sample(population, k)
n = 10
print("Square numbers:", [x**2 for x in range(n)])