import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))