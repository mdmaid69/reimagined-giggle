import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)