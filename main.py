import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height