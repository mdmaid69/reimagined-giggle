import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h