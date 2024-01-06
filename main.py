import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)