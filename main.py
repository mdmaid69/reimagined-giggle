def calculate_roi(gain, cost):
        return (gain - cost) / cost
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h