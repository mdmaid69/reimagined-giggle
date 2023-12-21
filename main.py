import random
def roll_die():
        return random.randint(1, 6)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)