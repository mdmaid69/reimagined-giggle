import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h