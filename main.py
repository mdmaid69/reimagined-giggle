def calculate_pressure(force, area):
        return force / area
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h