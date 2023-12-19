import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)