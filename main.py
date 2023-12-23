import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h