import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
def calculate_roi(gain, cost):
        return (gain - cost) / cost