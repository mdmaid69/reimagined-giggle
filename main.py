import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3