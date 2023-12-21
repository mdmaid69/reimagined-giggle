import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"