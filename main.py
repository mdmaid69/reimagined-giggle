import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)