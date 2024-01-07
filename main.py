import math
def calculate_absolute_value(x):
        return math.fabs(x)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)