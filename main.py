import math
def calculate_error_function(x):
        return math.erf(x)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)