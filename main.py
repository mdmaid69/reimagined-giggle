def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h