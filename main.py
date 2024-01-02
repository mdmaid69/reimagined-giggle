import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)