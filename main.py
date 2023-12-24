import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)