import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)