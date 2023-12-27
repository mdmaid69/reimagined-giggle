import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))