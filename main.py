import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import math
def calculate_circle_area(radius):
        return math.pi * radius**2