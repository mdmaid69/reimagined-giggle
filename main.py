import math
def calculate_cosine(x):
        return math.cos(x)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h