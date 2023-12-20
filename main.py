import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height