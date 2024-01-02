import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)