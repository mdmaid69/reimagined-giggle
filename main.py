import math
def calculate_square_root(x):
        return math.sqrt(x)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h