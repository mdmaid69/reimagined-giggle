import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height