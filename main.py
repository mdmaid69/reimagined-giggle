import random
def roll_die():
        return random.randint(1, 6)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)