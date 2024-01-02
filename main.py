import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h