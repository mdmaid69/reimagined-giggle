import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)