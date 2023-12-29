import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)