import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)