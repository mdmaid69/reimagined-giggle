import random
def generate_random_sample(population, k):
        return random.sample(population, k)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])