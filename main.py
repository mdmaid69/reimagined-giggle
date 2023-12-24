import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)