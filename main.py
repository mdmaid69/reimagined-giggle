import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)