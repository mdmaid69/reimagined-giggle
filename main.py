import random
def generate_random_sample(population, k):
        return random.sample(population, k)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])