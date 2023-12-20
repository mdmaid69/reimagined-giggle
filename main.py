import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def calculate_density(mass, volume):
        return mass / volume