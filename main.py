import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)