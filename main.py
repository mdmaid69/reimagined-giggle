import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)