import random
def roll_die():
        return random.randint(1, 6)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)