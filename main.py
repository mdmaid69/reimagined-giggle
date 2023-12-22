import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import random
def generate_random_choice(choices):
        return random.choice(choices)