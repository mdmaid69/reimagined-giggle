import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)