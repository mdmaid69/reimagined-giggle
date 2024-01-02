import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
def calculate_roi(gain, cost):
        return (gain - cost) / cost