import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)