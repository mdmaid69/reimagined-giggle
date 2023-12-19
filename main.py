import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)