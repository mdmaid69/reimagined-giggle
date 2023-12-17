import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"