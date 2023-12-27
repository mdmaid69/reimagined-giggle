import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def calculate_work(force, distance):
        return force * distance