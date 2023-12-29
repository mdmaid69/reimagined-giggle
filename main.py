import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)