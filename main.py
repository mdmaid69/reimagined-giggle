import random
def generate_random_sample(population, k):
        return random.sample(population, k)
def calculate_roi(gain, cost):
        return (gain - cost) / cost