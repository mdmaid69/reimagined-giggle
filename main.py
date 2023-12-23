import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h