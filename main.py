import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)