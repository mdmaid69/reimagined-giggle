import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)