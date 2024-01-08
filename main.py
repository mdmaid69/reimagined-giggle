import random
def generate_random_sample(population, k):
        return random.sample(population, k)
def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5