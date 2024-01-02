import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)