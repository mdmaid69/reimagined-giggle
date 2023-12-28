import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)