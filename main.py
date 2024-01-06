import random
def generate_random_sample(population, k):
        return random.sample(population, k)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)