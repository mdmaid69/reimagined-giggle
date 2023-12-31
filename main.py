import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)