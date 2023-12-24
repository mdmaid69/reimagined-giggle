import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import random
def generate_random_choice(choices):
        return random.choice(choices)