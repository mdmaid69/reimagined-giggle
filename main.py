import random
def roll_die():
        return random.randint(1, 6)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)