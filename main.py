import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2