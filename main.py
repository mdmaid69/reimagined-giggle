import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h