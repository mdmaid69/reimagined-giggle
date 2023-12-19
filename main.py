import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius