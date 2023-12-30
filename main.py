def calculate_force(mass, acceleration):
        return mass * acceleration
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h