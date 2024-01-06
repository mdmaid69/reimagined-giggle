import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)