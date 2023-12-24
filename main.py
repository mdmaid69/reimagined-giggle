def calculate_power(work, time):
        return work / time
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h