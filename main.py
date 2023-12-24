def calculate_area(radius):
        return 3.14 * radius * radius
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h