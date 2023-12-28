import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)