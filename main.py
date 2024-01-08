import math
def calculate_error_function(x):
        return math.erf(x)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)