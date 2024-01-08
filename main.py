import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import random
def generate_random_number(start, end):
        return random.randint(start, end)