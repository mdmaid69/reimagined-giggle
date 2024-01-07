import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)