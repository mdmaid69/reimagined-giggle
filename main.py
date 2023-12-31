import random
def generate_random_choice(choices):
        return random.choice(choices)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)