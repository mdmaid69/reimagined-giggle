import math
def calculate_inverse_hyperbolic_tangent(x):
        return math.atanh(x)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h