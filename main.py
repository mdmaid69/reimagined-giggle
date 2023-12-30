import math
def calculate_hyperbolic_sine(x):
        return math.sinh(x)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h