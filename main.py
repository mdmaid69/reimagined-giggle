import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)