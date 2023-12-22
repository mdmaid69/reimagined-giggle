import math
def calculate_absolute_value(x):
        return math.fabs(x)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)