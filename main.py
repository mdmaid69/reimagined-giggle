import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def calculate_pressure(force, area):
        return force / area