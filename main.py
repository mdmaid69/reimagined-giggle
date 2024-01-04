import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)