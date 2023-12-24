import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)