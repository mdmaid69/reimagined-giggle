import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height