import random
def generate_random_sample(population, k):
        return random.sample(population, k)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)