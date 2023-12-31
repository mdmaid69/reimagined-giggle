import random
def roll_die():
        return random.randint(1, 6)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h