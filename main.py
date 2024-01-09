import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import random
def roll_die():
        return random.randint(1, 6)