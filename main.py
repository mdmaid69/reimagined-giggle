import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2