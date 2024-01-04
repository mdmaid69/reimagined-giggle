import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)