import collections
def create_queue():
        return collections.deque()
import random
def generate_random_sample(population, k):
        return random.sample(population, k)