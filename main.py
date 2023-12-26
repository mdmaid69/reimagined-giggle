import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
def calculate_roi(gain, cost):
        return (gain - cost) / cost