import math
def calculate_gamma_function(x):
        return math.gamma(x)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h