import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height