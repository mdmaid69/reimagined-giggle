import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import math
def calculate_complementary_error_function(x):
        return math.erfc(x)