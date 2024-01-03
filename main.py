import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)