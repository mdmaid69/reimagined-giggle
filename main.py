import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3