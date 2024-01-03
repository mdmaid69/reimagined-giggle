import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)