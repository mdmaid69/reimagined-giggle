import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))