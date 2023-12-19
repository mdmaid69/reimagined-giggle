import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import math
def calculate_arc_tangent(x):
        return math.atan(x)