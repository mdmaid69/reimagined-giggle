import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import random
def generate_random_sample(population, k):
        return random.sample(population, k)