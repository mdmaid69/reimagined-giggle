import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h