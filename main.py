import random
def generate_random_number(start, end):
        return random.randint(start, end)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)