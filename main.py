import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import math
def calculate_hyperbolic_cosine(x):
        return math.cosh(x)