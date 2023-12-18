import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height