import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)