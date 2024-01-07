import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import random
def generate_random_choice(choices):
        return random.choice(choices)