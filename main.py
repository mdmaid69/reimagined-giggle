import random
def generate_random_number(start, end):
        return random.randint(start, end)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h