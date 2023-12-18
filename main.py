import random
def generate_random_sample(population, k):
        return random.sample(population, k)
def remove_duplicates(lst):
        return list(set(lst))