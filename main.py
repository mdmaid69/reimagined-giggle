def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)