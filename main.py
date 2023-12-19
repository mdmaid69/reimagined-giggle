def calculate_average(lst):
        return sum(lst) / len(lst)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h