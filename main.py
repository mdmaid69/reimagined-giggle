import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))