import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
def calculate_density(mass, volume):
        return mass / volume