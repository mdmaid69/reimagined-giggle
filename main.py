import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h