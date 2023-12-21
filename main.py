def calculate_perpetuity(payment, rate):
        return payment / rate
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h