import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)