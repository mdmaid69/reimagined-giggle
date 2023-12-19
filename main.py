import random
def generate_random_sample(population, k):
        return random.sample(population, k)
def find_union(list1, list2):
        return set(list1) | set(list2)