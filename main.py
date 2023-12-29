def calculate_density(mass, volume):
        return mass / volume
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h