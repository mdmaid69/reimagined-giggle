import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius