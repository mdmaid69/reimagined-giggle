import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def calculate_pressure(force, area):
        return force / area